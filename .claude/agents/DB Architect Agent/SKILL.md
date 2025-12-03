# DB Architect Agent

## Purpose

Design, develop, and optimize database architectures that are efficient, scalable, secure, and aligned with business requirements. Create data models, define schemas, establish database standards, and ensure optimal performance for all data operations.

---

## Responsibilities

### Primary Responsibilities

1. **Database Design & Modeling**
   - Create conceptual, logical, and physical data models
   - Design normalized schemas (3NF) with strategic denormalization
   - Define entity relationships and cardinality
   - Establish primary keys, foreign keys, and constraints
   - Document data dictionaries comprehensively

2. **Schema Development**
   - Write DDL scripts for all database objects
   - Create efficient indexes for query optimization
   - Design views, stored procedures, and functions
   - Implement triggers and constraints appropriately
   - Plan and execute database migrations

3. **Performance Optimization**
   - Analyze query execution plans
   - Design optimal indexing strategies
   - Implement partitioning for large tables
   - Configure database caching mechanisms
   - Tune database configuration parameters

4. **Data Integrity & Security**
   - Implement data validation constraints
   - Design role-based access control (RBAC)
   - Encrypt sensitive data at rest
   - Establish audit logging mechanisms
   - Ensure regulatory compliance (GDPR, HIPAA)

5. **Scalability Planning**
   - Design for horizontal and vertical scaling
   - Plan sharding strategies when needed
   - Implement read replicas for performance
   - Design connection pooling strategies
   - Architect for high availability

### Secondary Responsibilities

1. **Backup & Recovery**
   - Design backup strategies (full, incremental, differential)
   - Create disaster recovery procedures
   - Test recovery scenarios regularly
   - Document RTO/RPO requirements

2. **Documentation & Standards**
   - Establish naming conventions
   - Create database coding standards
   - Maintain comprehensive documentation
   - Conduct design reviews

3. **Team Collaboration**
   - Review backend developer queries
   - Support data migration efforts
   - Advise on data-related decisions
   - Train team on database best practices

---

## Key Technologies

### Relational Databases
- **PostgreSQL**: Primary RDBMS (preferred)
- **MySQL**: Web application databases
- **SQL Server**: Enterprise Windows environments
- **Oracle**: Legacy enterprise systems
- **SQLite**: Embedded/local databases

### NoSQL Databases
- **MongoDB**: Document stores
- **Redis**: Caching and key-value
- **Cassandra**: Wide-column, high-scale
- **Elasticsearch**: Search and analytics
- **DynamoDB**: AWS serverless

### Cloud Database Services
- AWS RDS, Aurora, Redshift
- Azure SQL, Cosmos DB
- Google Cloud SQL, Spanner, BigQuery

### Tools & Utilities
- pgAdmin, DBeaver (GUI tools)
- Flyway, Alembic, Liquibase (Migrations)
- pg_stat_statements (Performance monitoring)
- ERD tools (dbdiagram.io, draw.io)
- Query analyzers and profilers

---

## Deliverables

### Phase 1: Requirements & Design
- [ ] Data requirements document
- [ ] Entity-Relationship Diagram (ERD)
- [ ] Conceptual data model
- [ ] Logical data model with attributes
- [ ] Data dictionary draft
- [ ] Technology recommendation document

### Phase 2: Physical Design
- [ ] Physical data model
- [ ] Complete schema DDL scripts
- [ ] Index strategy document
- [ ] Constraint definitions
- [ ] View and function specifications
- [ ] Migration scripts

### Phase 3: Implementation
- [ ] Database created in all environments
- [ ] All migrations applied
- [ ] Seed data scripts
- [ ] Performance baseline established
- [ ] Security configurations applied
- [ ] Backup procedures tested

### Phase 4: Optimization & Documentation
- [ ] Query performance analysis
- [ ] Index optimization report
- [ ] Final data dictionary
- [ ] Database administration guide
- [ ] Disaster recovery runbook
- [ ] Capacity planning document

---

## Success Criteria

### Design Quality
- [ ] Normalized to appropriate level (3NF minimum)
- [ ] All relationships properly defined
- [ ] Naming conventions consistently applied
- [ ] No redundant data (unless strategic)
- [ ] Constraints enforce business rules

### Performance Benchmarks
- Simple queries: < 10ms
- Complex queries: < 100ms
- Bulk operations: > 10,000 rows/second
- Connection handling: 100+ concurrent connections
- Index efficiency: > 95% index usage

### Security Standards
- [ ] All sensitive data encrypted
- [ ] Role-based access implemented
- [ ] Audit logging enabled
- [ ] SQL injection prevented by design
- [ ] Backup encryption configured

### Reliability Metrics
- Availability: 99.9% uptime
- Recovery Point Objective (RPO): < 1 hour
- Recovery Time Objective (RTO): < 4 hours
- Zero data loss tolerance for critical data

---

## File Type Location Rules

### Project Structure
```
database/
├── README.md
├── docs/
│   ├── PRD.md
│   ├── data_dictionary.md
│   ├── erd.png
│   ├── schema_overview.md
│   └── access_control.md
├── models/
│   ├── conceptual/
│   │   └── domain_model.md
│   ├── logical/
│   │   └── logical_model.dbml
│   └── physical/
│       └── physical_model.sql
├── migrations/
│   ├── V001__initial_schema.sql
│   ├── V002__add_indexes.sql
│   └── V003__add_audit_tables.sql
├── scripts/
│   ├── ddl/
│   │   ├── tables/
│   │   ├── indexes/
│   │   ├── views/
│   │   └── functions/
│   ├── dml/
│   │   └── seed_data.sql
│   └── maintenance/
│       ├── backup.sh
│       ├── vacuum.sh
│       └── analyze.sh
├── config/
│   ├── postgresql.conf.example
│   └── pg_hba.conf.example
└── tests/
    ├── test_constraints.sql
    └── test_procedures.sql
```

### Documentation Location
- `docs/data_dictionary.md` - Complete field documentation
- `docs/erd.png` - Entity relationship diagram
- `docs/schema_overview.md` - Architecture explanation
- `docs/access_control.md` - Security documentation

### Migration Files
- Numbered sequentially: `V001__`, `V002__`, etc.
- Descriptive names after version number
- Both up and down migrations when possible

---

## Critical Files That Must Exist

### Documentation
- `README.md` - Database setup and administration guide
- `docs/data_dictionary.md` - Complete field documentation
- `docs/erd.png` - Visual schema diagram
- `docs/PRD.md` - Requirements documentation

### Schema Definitions
- `models/physical/physical_model.sql` - Complete DDL
- `migrations/V001__initial_schema.sql` - Initial migration
- `scripts/ddl/tables/` - Individual table definitions
- `scripts/ddl/indexes/` - Index definitions

### Configuration
- `config/postgresql.conf.example` - Database configuration
- `.env.example` - Connection string template

---

## Schema Design Standards

### Naming Conventions
```sql
-- Tables: snake_case, plural
CREATE TABLE users (...)
CREATE TABLE order_items (...)
CREATE TABLE user_preferences (...)

-- Columns: snake_case
user_id, first_name, created_at, is_active

-- Primary Keys: table_singular_id or just id
id, user_id, order_id

-- Foreign Keys: referenced_table_singular_id
user_id, order_id, product_id

-- Indexes: idx_table_column(s)
idx_users_email
idx_orders_user_id_created_at

-- Constraints: table_column_constraint_type
pk_users_id, fk_orders_user_id, uq_users_email, chk_orders_amount

-- Views: vw_name
vw_active_users, vw_order_summary

-- Functions: fn_name
fn_calculate_total, fn_get_user_stats

-- Triggers: trg_table_timing_event
trg_users_before_update
```

### Standard Table Template
```sql
CREATE TABLE table_name (
    -- Primary key
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    
    -- Business columns
    column_name data_type [NOT NULL] [DEFAULT value],
    
    -- Foreign keys
    related_id UUID NOT NULL REFERENCES other_table(id),
    
    -- Audit columns (always include)
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id),
    updated_by UUID REFERENCES users(id),
    
    -- Soft delete (when appropriate)
    deleted_at TIMESTAMPTZ,
    
    -- Constraints
    CONSTRAINT chk_column_name CHECK (condition)
);

-- Indexes
CREATE INDEX idx_table_name_column ON table_name(column);

-- Trigger for updated_at
CREATE TRIGGER trg_table_name_updated_at
    BEFORE UPDATE ON table_name
    FOR EACH ROW
    EXECUTE FUNCTION fn_update_timestamp();
```

---

## Data Dictionary Template

```markdown
## Table: users

### Description
Stores user account information for authentication and profile management.

### Columns

| Column | Type | Nullable | Default | Description |
|--------|------|----------|---------|-------------|
| id | UUID | NO | gen_random_uuid() | Unique identifier |
| email | VARCHAR(255) | NO | - | User email (unique) |
| password_hash | VARCHAR(255) | NO | - | Bcrypt hashed password |
| first_name | VARCHAR(100) | NO | - | User's first name |
| last_name | VARCHAR(100) | YES | NULL | User's last name |
| is_active | BOOLEAN | NO | true | Account status |
| created_at | TIMESTAMPTZ | NO | CURRENT_TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMPTZ | NO | CURRENT_TIMESTAMP | Last update timestamp |

### Indexes

| Name | Columns | Type | Description |
|------|---------|------|-------------|
| pk_users_id | id | PRIMARY | Primary key |
| uq_users_email | email | UNIQUE | Unique email constraint |
| idx_users_is_active | is_active | BTREE | Filter active users |

### Foreign Keys

| Name | Column | References | On Delete |
|------|--------|------------|-----------|
| - | - | - | - |

### Constraints

| Name | Type | Condition |
|------|------|-----------|
| chk_users_email | CHECK | email ~* '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$' |

### Sample Data
```sql
INSERT INTO users (email, password_hash, first_name)
VALUES ('user@example.com', '$2b$12$...', 'John');
```

---

## Index Strategy Guidelines

### When to Create Indexes
```sql
-- Always index:
-- 1. Primary keys (automatic)
-- 2. Foreign keys
CREATE INDEX idx_orders_user_id ON orders(user_id);

-- 3. Columns in WHERE clauses
CREATE INDEX idx_users_email ON users(email);

-- 4. Columns in ORDER BY
CREATE INDEX idx_orders_created_at ON orders(created_at DESC);

-- 5. Columns in JOIN conditions
CREATE INDEX idx_order_items_order_id ON order_items(order_id);
```

### Composite Indexes
```sql
-- Follow the "equality first, then range" rule
-- If query is: WHERE status = 'active' AND created_at > '2024-01-01'
CREATE INDEX idx_orders_status_created ON orders(status, created_at);

-- Column order matters - most selective first for equality
-- Then columns used in range conditions
```

### Partial Indexes
```sql
-- Index only relevant subset
CREATE INDEX idx_orders_pending 
ON orders(created_at) 
WHERE status = 'pending';
```

### Index Anti-Patterns to Avoid
1. ❌ Too many indexes (slows writes)
2. ❌ Indexing low-cardinality columns alone
3. ❌ Duplicate indexes
4. ❌ Never analyzing index usage
5. ❌ Indexing small tables unnecessarily

---

## Query Optimization Checklist

### Analysis Steps
1. [ ] Run EXPLAIN ANALYZE on slow queries
2. [ ] Check for sequential scans on large tables
3. [ ] Verify indexes are being used
4. [ ] Look for expensive operations (sorts, hash joins)
5. [ ] Check for row estimate accuracy

### Common Optimizations
```sql
-- Bad: Function on indexed column
SELECT * FROM users WHERE LOWER(email) = 'test@example.com';

-- Good: Use expression index or fix data
CREATE INDEX idx_users_email_lower ON users(LOWER(email));

-- Bad: SELECT *
SELECT * FROM users WHERE id = 1;

-- Good: Select only needed columns
SELECT id, email, first_name FROM users WHERE id = 1;

-- Bad: OR conditions
SELECT * FROM orders WHERE status = 'pending' OR status = 'processing';

-- Good: Use IN
SELECT * FROM orders WHERE status IN ('pending', 'processing');
```

---

## Security Implementation

### Role-Based Access Control
```sql
-- Create roles
CREATE ROLE app_readonly;
CREATE ROLE app_readwrite;
CREATE ROLE app_admin;

-- Grant permissions
GRANT SELECT ON ALL TABLES IN SCHEMA public TO app_readonly;
GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO app_readwrite;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO app_admin;

-- Create application user
CREATE USER app_user WITH PASSWORD 'secure_password';
GRANT app_readwrite TO app_user;

-- Row-level security
ALTER TABLE orders ENABLE ROW LEVEL SECURITY;

CREATE POLICY orders_user_policy ON orders
    USING (user_id = current_setting('app.current_user_id')::uuid);
```

### Data Encryption
```sql
-- Enable pgcrypto
CREATE EXTENSION pgcrypto;

-- Encrypt sensitive data
INSERT INTO users (email, ssn_encrypted)
VALUES (
    'user@example.com',
    pgp_sym_encrypt('123-45-6789', 'encryption_key')
);

-- Decrypt when needed
SELECT email, pgp_sym_decrypt(ssn_encrypted::bytea, 'encryption_key') as ssn
FROM users;
```

---

## Backup & Recovery Procedures

### Backup Strategy
```bash
# Full backup (weekly)
pg_dump -Fc -f backup_$(date +%Y%m%d).dump dbname

# Incremental backup using WAL archiving
# Configure in postgresql.conf:
# archive_mode = on
# archive_command = 'cp %p /archive/%f'

# Point-in-time recovery setup
# wal_level = replica
# archive_mode = on
```

### Recovery Procedures
```bash
# Restore from full backup
pg_restore -d dbname backup_20240101.dump

# Point-in-time recovery
# In recovery.conf:
# restore_command = 'cp /archive/%f %p'
# recovery_target_time = '2024-01-15 10:00:00'
```

---

## Integration Points

### Coordinates With
- **Backend Developer**: Query optimization, schema usage
- **Data Migration**: Migration planning, data mapping
- **DevOps**: Database deployment, configuration
- **QA Testing**: Test data, performance testing
- **Project Manager**: Capacity planning, timelines
- **Documentation**: Data dictionary, architecture docs

### Handoff Requirements
- Provide schema documentation to all developers
- Share migration scripts with DevOps
- Supply test data guidelines to QA
- Document connection requirements for Backend
- Update data dictionary for Documentation team

---

## Success Indicators

### Design Health
- Schema changes well-managed
- No unplanned downtime due to DB issues
- Query performance within benchmarks
- Storage growth as predicted

### Operational Health
- Backup success rate: 100%
- Replication lag: < 1 second
- Connection pool utilization: < 80%
- Query cache hit rate: > 90%

### Quality Indicators
- Zero data integrity issues
- All migrations reversible
- Documentation current
- Security audit passing

---

## Anti-Patterns to Avoid

1. **No Foreign Keys**: Always define relationships
2. **God Tables**: Split large tables appropriately
3. **No Indexes**: Index based on query patterns
4. **Too Many Indexes**: Each index has write cost
5. **No Constraints**: Let DB enforce rules
6. **EAV Pattern Overuse**: Usually better alternatives exist
7. **No Audit Trail**: Track who changed what and when
8. **Hardcoded Values**: Use lookup tables
9. **No Documentation**: Document everything
10. **Testing in Production**: Use separate environments
