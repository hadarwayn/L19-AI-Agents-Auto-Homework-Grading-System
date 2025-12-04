"""
Ring Buffer Logging System

Implements a rotating log file system with:
- Maximum lines per file (default: 1000)
- Maximum number of log files (default: 5)
- Automatic rotation when limits are reached

Author: Hadar Wayn
Date: December 2025
"""

import json
import logging
import os
from pathlib import Path
from typing import Optional

from .paths import get_logs_dir, get_log_config_dir


class RingBufferHandler(logging.Handler):
    """Custom logging handler that implements ring buffer behavior"""
    def __init__(self, log_dir: Path, max_lines: int = 1000, max_files: int = 5, filename_prefix: str = "app"):
        """Initialize ring buffer handler"""
        super().__init__()
        self.log_dir = log_dir
        self.max_lines = max_lines
        self.max_files = max_files
        self.filename_prefix = filename_prefix
        self.current_file_index = 0
        self.current_line_count = 0
        self.log_dir.mkdir(parents=True, exist_ok=True)
        self._find_current_log()

    def _find_current_log(self):
        """Find the most recent log file and its line count"""
        existing_logs = sorted(self.log_dir.glob(f"{self.filename_prefix}_*.log"))
        if existing_logs:
            latest_log = existing_logs[-1]
            index_str = latest_log.stem.split("_")[-1]
            try:
                self.current_file_index = int(index_str)
            except ValueError:
                self.current_file_index = 0
            try:
                with open(latest_log, "r") as f:
                    self.current_line_count = sum(1 for _ in f)
            except Exception:
                self.current_line_count = 0

    def _get_current_log_path(self) -> Path:
        """Get path to current log file"""
        return self.log_dir / f"{self.filename_prefix}_{self.current_file_index:03d}.log"

    def _rotate(self):
        """Rotate to next log file"""
        self.current_file_index = (self.current_file_index + 1) % self.max_files
        self.current_line_count = 0
        log_path = self._get_current_log_path()
        if log_path.exists():
            log_path.unlink()

    def emit(self, record):
        """Emit a log record"""
        try:
            if self.current_line_count >= self.max_lines:
                self._rotate()
            msg = self.format(record)
            log_path = self._get_current_log_path()
            with open(log_path, "a") as f:
                f.write(msg + "\n")
            self.current_line_count += 1
        except Exception:
            self.handleError(record)


def setup_logger(name: str) -> logging.Logger:
    """Setup a logger with ring buffer handler"""
    log_config_path = get_log_config_dir() / "log_config.json"
    try:
        with open(log_config_path, "r") as f:
            config = json.load(f)
        ring_buffer_config = config.get("ring_buffer", {})
    except Exception:
        ring_buffer_config = {}
    max_lines = ring_buffer_config.get("max_lines_per_file", 1000)
    max_files = ring_buffer_config.get("max_log_files", 5)
    log_level = ring_buffer_config.get("log_level", "INFO")
    log_format = ring_buffer_config.get("format", "%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    date_format = ring_buffer_config.get("date_format", "%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, log_level))
    logger.handlers.clear()
    handler = RingBufferHandler(
        log_dir=get_logs_dir(),
        max_lines=max_lines,
        max_files=max_files,
        filename_prefix=name.replace(".", "_")
    )
    formatter = logging.Formatter(log_format, date_format)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_log_status() -> dict:
    """Get current logging status"""
    log_dir = get_logs_dir()
    log_files = sorted(log_dir.glob("*.log"))

    return {
        "log_directory": str(log_dir),
        "total_files": len(log_files),
        "files": [{"name": f.name, "size": f.stat().st_size} for f in log_files]
    }
