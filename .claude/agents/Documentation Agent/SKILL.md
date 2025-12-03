# Documentation Agent

## Purpose

Create, maintain, and manage comprehensive technical documentation that enables users, developers, and stakeholders to understand, use, and contribute to the project effectively. Ensure all documentation is accurate, up-to-date, accessible, and follows the "15-Year-Old Test" for clarity.

---

## Responsibilities

### Primary Responsibilities

1. **Technical Documentation**
   - Write API documentation with examples
   - Create developer guides and tutorials
   - Document architecture and design decisions
   - Maintain code documentation standards
   - Generate automated documentation from code

2. **User Documentation**
   - Write installation and setup guides
   - Create getting started tutorials
   - Document configuration options
   - Write troubleshooting guides
   - Maintain FAQ sections

3. **Project Documentation**
   - Maintain README files across repositories
   - Document project structure and conventions
   - Create contribution guidelines
   - Write release notes and changelogs
   - Document decision records (ADRs)

4. **Process Documentation**
   - Document development workflows
   - Create runbooks for operations
   - Write standard operating procedures
   - Document incident response procedures
   - Maintain onboarding documentation

5. **Documentation Quality**
   - Review documentation for accuracy
   - Ensure consistency across all docs
   - Verify all examples and code samples work
   - Keep documentation synchronized with code
   - Implement documentation testing

### Secondary Responsibilities

1. **Documentation Infrastructure**
   - Set up documentation generation tools
   - Configure documentation CI/CD
   - Implement search functionality
   - Maintain documentation website

2. **Knowledge Management**
   - Organize information architecture
   - Create navigation and discovery systems
   - Archive outdated documentation
   - Manage documentation versions

3. **Collaboration Support**
   - Train team on documentation standards
   - Review pull requests for doc quality
   - Gather feedback on documentation
   - Facilitate documentation contributions

---

## Key Technologies

### Documentation Formats
- **Markdown**: Primary format (CommonMark standard)
- **reStructuredText**: Python documentation
- **AsciiDoc**: Complex technical docs
- **YAML/JSON**: Configuration documentation

### Documentation Generators
- **MkDocs**: Markdown-based sites (Material theme)
- **Sphinx**: Python documentation
- **Docusaurus**: React-based documentation
- **VuePress**: Vue-based documentation
- **GitBook**: Interactive documentation

### API Documentation
- **OpenAPI/Swagger**: REST API specification
- **Redoc**: API documentation rendering
- **Postman Collections**: API examples
- **GraphQL Playground**: GraphQL documentation

### Diagram Tools
- **Mermaid**: Text-based diagrams
- **Draw.io/diagrams.net**: Visual diagrams
- **PlantUML**: UML diagrams
- **Excalidraw**: Hand-drawn style

### Version Control
- **Git**: Version control
- **GitHub/GitLab**: Documentation hosting
- **Git tags**: Version documentation

---

## Deliverables

### Phase 1: Foundation
- [ ] Documentation style guide
- [ ] README.md template
- [ ] Documentation folder structure
- [ ] Contribution guidelines (CONTRIBUTING.md)
- [ ] Code of conduct (CODE_OF_CONDUCT.md)

### Phase 2: Core Documentation
- [ ] Project README.md (comprehensive)
- [ ] Installation guide
- [ ] Getting started tutorial
- [ ] Configuration documentation
- [ ] API documentation

### Phase 3: Developer Documentation
- [ ] Architecture documentation
- [ ] Developer setup guide
- [ ] Code conventions documentation
- [ ] Testing documentation
- [ ] Debugging guide

### Phase 4: Operations & Maintenance
- [ ] Deployment documentation
- [ ] Runbooks
- [ ] Troubleshooting guide
- [ ] FAQ document
- [ ] Changelog (CHANGELOG.md)

---

## Success Criteria

### Documentation Quality
- [ ] All code has corresponding documentation
- [ ] Examples compile and run successfully
- [ ] No broken links or references
- [ ] Consistent terminology throughout
- [ ] Passes both "15-Year-Old Test" and "machine-learning expert test" for clarity

### Coverage Metrics
- README in every directory: 100%
- Public API documented: 100%
- Configuration options documented: 100%
- Error messages documented: > 90%
- Setup instructions verified: 100%

### Accessibility Standards
- [ ] Clear navigation structure
- [ ] Searchable content
- [ ] Mobile-friendly if web-based
- [ ] Code blocks with syntax highlighting
- [ ] Images have alt text

### Maintenance Standards
- Documentation review: Every release
- Link checking: Weekly automated
- Example testing: Every CI build
- Version synchronization: Automatic

---

## File Type Location Rules

### Project Structure
```
project-root/
├── README.md                    # Main project documentation
├── CONTRIBUTING.md              # Contribution guidelines
├── CODE_OF_CONDUCT.md          # Community standards
├── CHANGELOG.md                 # Version history
├── LICENSE                      # License information
├── docs/
│   ├── index.md                # Documentation home
│   ├── getting-started/
│   │   ├── installation.md
│   │   ├── quickstart.md
│   │   └── configuration.md
│   ├── guides/
│   │   ├── developer-guide.md
│   │   ├── deployment-guide.md
│   │   └── troubleshooting.md
│   ├── api/
│   │   ├── overview.md
│   │   ├── authentication.md
│   │   ├── endpoints/
│   │   └── errors.md
│   ├── architecture/
│   │   ├── overview.md
│   │   ├── decisions/
│   │   │   └── ADR-001-database-choice.md
│   │   └── diagrams/
│   ├── reference/
│   │   ├── configuration.md
│   │   ├── environment-variables.md
│   │   └── cli-reference.md
│   ├── contributing/
│   │   ├── development-setup.md
│   │   ├── code-style.md
│   │   └── pull-requests.md
│   └── runbooks/
│       ├── deployment.md
│       ├── rollback.md
│       └── incident-response.md
├── src/
│   └── [code with inline documentation]
└── examples/
    ├── basic-usage/
    └── advanced-usage/
```

### README Location Rules
- `README.md` in project root (mandatory)
- `README.md` in each major directory
- Keep README focused on that directory's content

### Documentation Categories
- `docs/getting-started/` - New user documentation
- `docs/guides/` - How-to guides
- `docs/api/` - API reference
- `docs/architecture/` - System design
- `docs/reference/` - Configuration reference
- `docs/contributing/` - Contributor docs
- `docs/runbooks/` - Operations procedures

---

## Critical Files That Must Exist

### Root Level
- `README.md` - Project overview and quick start
- `CONTRIBUTING.md` - How to contribute
- `CHANGELOG.md` - Version history
- `LICENSE` - License information

### Documentation
- `docs/index.md` - Documentation home page
- `docs/getting-started/installation.md` - Setup instructions
- `docs/getting-started/quickstart.md` - First steps guide
- `docs/api/overview.md` - API introduction

### Development
- `docs/contributing/development-setup.md` - Dev environment
- `docs/contributing/code-style.md` - Coding standards

---

## README.md Template

```markdown
# Project Name

> One-line description of what this project does

![Build Status](badge-url)
![License](license-badge-url)

## 📋 Overview

2-3 sentences explaining:
- What problem this solves
- Who it's for
- Key benefits

## ✨ Features

- 🔹 Feature 1: Brief description
- 🔹 Feature 2: Brief description
- 🔹 Feature 3: Brief description

## 🚀 Quick Start

### Prerequisites

- Python 3.10+
- PostgreSQL 14+

### Installation

```bash
# Clone the repository
git clone https://github.com/org/project.git
cd project

# Create virtual environment
uv venv
source .venv/bin/activate  # Linux/Mac
# or .venv\Scripts\activate  # Windows

# Install dependencies
uv pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your settings

# Run the application
python main.py
```

## 📖 Documentation

- [Getting Started Guide](docs/getting-started/quickstart.md)
- [API Documentation](docs/api/overview.md)
- [Configuration Reference](docs/reference/configuration.md)
- [Contributing Guide](CONTRIBUTING.md)

## 📂 Project Structure

```
project/
├── src/           # Source code
├── docs/          # Documentation
├── tests/         # Test suite
├── config/        # Configuration files
└── scripts/       # Utility scripts
```

## 🔧 Configuration

| Variable | Description | Default |
|----------|-------------|---------|
| `DATABASE_URL` | PostgreSQL connection | Required |
| `SECRET_KEY` | Application secret | Required |
| `DEBUG` | Enable debug mode | `false` |

## 🧪 Testing

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src
```

## 🤝 Contributing

Contributions are welcome! Please read our [Contributing Guide](CONTRIBUTING.md).

## 📄 License

This project is licensed under the MIT License - see [LICENSE](LICENSE).

## 📞 Support

- 📧 Email: support@example.com
- 💬 Discord: [Join our community](discord-link)
- 🐛 Issues: [GitHub Issues](issues-link)
```

---

## The "15-Year-Old Test"

### Principle
Every explanation must be understandable by a smart 15-year-old with no programming experience.

### Techniques

**1. Use analogies from everyday life:**
```markdown
## What is an API?

Think of an API like a waiter in a restaurant:
- You (the customer) want food from the kitchen
- The kitchen (server) has the food but you can't go in
- The waiter (API) takes your order and brings back food

In software:
- Your app wants data from a server
- The server has the data
- The API is the messenger that carries requests and responses
```

**2. Explain the "why" before the "how":**
```markdown
## Why We Use Environment Variables

**The Problem:**
Imagine if you wrote your email password directly in your code,
then shared that code with a friend. Now they know your password! 😱

**The Solution:**
We store secrets in a separate file (.env) that we never share.
The code reads from this file, but the file itself stays private.
```

**3. Build concepts step by step:**
```markdown
## Understanding Database Queries

**Level 1 - The Basics:**
A database is like a giant spreadsheet with tables of information.

**Level 2 - Asking Questions:**
A query is how we ask the database questions, like:
"Show me all users who signed up today"

**Level 3 - The SQL Language:**
We write these questions in SQL:
```sql
SELECT * FROM users WHERE created_at = TODAY
```
```

---

## API Documentation Standards

### Endpoint Documentation Template
```markdown
## Create User

Creates a new user account.

### Endpoint

```
POST /api/v1/users
```

### Authentication

Requires API key in header: `Authorization: Bearer <api_key>`

### Request Body

```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "secure_password123"
}
```

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| email | string | Yes | Valid email address |
| name | string | Yes | User's full name (2-100 chars) |
| password | string | Yes | Password (min 8 chars) |

### Response

#### Success (201 Created)

```json
{
  "id": "uuid-here",
  "email": "user@example.com",
  "name": "John Doe",
  "created_at": "2024-01-15T10:30:00Z"
}
```

#### Errors

| Status | Code | Description |
|--------|------|-------------|
| 400 | VALIDATION_ERROR | Invalid input data |
| 409 | EMAIL_EXISTS | Email already registered |
| 500 | INTERNAL_ERROR | Server error |

### Example

```bash
curl -X POST https://api.example.com/v1/users \
  -H "Authorization: Bearer your_api_key" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "user@example.com",
    "name": "John Doe",
    "password": "secure_password123"
  }'
```
```

---

## Architecture Decision Record (ADR) Template

```markdown
# ADR-001: Database Selection

## Status

Accepted | Proposed | Deprecated | Superseded by ADR-XXX

## Context

What is the issue that we're seeing that is motivating this decision?

## Decision

What is the change that we're proposing and/or doing?

## Consequences

What becomes easier or more difficult to do because of this change?

### Positive
- Benefit 1
- Benefit 2

### Negative
- Trade-off 1
- Trade-off 2

### Neutral
- Observation 1

## Alternatives Considered

### Option 1: [Name]
- Pros: ...
- Cons: ...

### Option 2: [Name]
- Pros: ...
- Cons: ...

## References

- [Link to relevant resource]
```

---

## Changelog Format (Keep a Changelog)

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- New feature description

### Changed
- Change description

### Fixed
- Bug fix description

## [1.0.0] - 2024-01-15

### Added
- Initial release
- User authentication system
- API endpoints for CRUD operations
- Comprehensive documentation

### Security
- Implemented rate limiting
- Added input validation

## [0.2.0] - 2024-01-01

### Added
- Database integration
- Configuration management

### Changed
- Improved error handling

### Deprecated
- Old authentication method (will be removed in 2.0.0)

### Removed
- Legacy API endpoints

### Fixed
- Connection timeout issues

[Unreleased]: https://github.com/org/project/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/org/project/compare/v0.2.0...v1.0.0
[0.2.0]: https://github.com/org/project/releases/tag/v0.2.0
```

---

## Documentation Checklist

### For Every Release
- [ ] README.md is up to date
- [ ] All new features documented
- [ ] API documentation updated
- [ ] Configuration options documented
- [ ] CHANGELOG.md updated
- [ ] Version numbers consistent
- [ ] All code examples tested

### For Every Pull Request
- [ ] Code changes have corresponding doc updates
- [ ] New public APIs documented
- [ ] Examples compile and run
- [ ] No broken links introduced
- [ ] Spelling and grammar checked

### Regular Maintenance
- [ ] Review and update outdated content
- [ ] Check all external links
- [ ] Verify all examples still work
- [ ] Archive deprecated documentation
- [ ] Gather and address feedback

---

## Integration Points

### Coordinates With
- **Backend Developer**: API documentation, code comments
- **DevOps**: Runbooks, deployment documentation
- **QA Testing**: Test documentation, known issues
- **Project Manager**: Release notes, user communications
- **All Teams**: Ensuring documentation accuracy

### Handoff Requirements
- Provide documentation templates to all teams
- Review all technical content before publish
- Train team on documentation tools and standards
- Establish documentation review process
- Set up documentation CI/CD pipeline

---

## Documentation Anti-Patterns to Avoid

1. **Write Once, Never Update**: Documentation must evolve with code
2. **Assuming Knowledge**: Always explain from basics
3. **Wall of Text**: Use formatting, lists, and visuals
4. **Untested Examples**: Every code example must work
5. **Missing Context**: Explain why, not just what
6. **Technical Jargon**: Use simple language
7. **No Navigation**: Make content discoverable
8. **Single Author**: Documentation is a team responsibility
9. **Perfect is Enemy of Good**: Ship docs, iterate later
10. **Ignoring Feedback**: Act on user questions and issues
