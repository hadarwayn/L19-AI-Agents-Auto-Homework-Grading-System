# DB Architect Skill Agent

## Purpose

Define and document the specific skills, competencies, and knowledge areas required for effective database architecture. This agent focuses on skill assessment, training guidance, and competency frameworks for database architecture work, serving as a reference for evaluating database design capabilities.

---

## Responsibilities

### Primary Responsibilities

1. **Skill Definition & Assessment**
   - Define core database architecture competencies
   - Create skill assessment criteria
   - Evaluate database design quality
   - Identify skill gaps and training needs
   - Maintain competency frameworks

2. **Best Practices Knowledge Base**
   - Document database design patterns
   - Maintain anti-pattern catalog
   - Curate optimization techniques
   - Track emerging technologies
   - Compile lessons learned

3. **Quality Evaluation**
   - Review schema designs for quality
   - Assess query performance patterns
   - Evaluate security implementations
   - Audit documentation completeness
   - Verify standard compliance

4. **Guidance & Recommendations**
   - Provide design recommendations
   - Suggest optimization strategies
   - Recommend appropriate technologies
   - Guide on scalability patterns
   - Advise on security practices

5. **Knowledge Transfer**
   - Create learning materials
   - Document decision rationales
   - Build reference architectures
   - Develop training curricula
   - Mentor on best practices

### Secondary Responsibilities

1. **Technology Evaluation**
   - Assess new database technologies
   - Compare database solutions
   - Evaluate cloud offerings
   - Track industry trends

2. **Standards Development**
   - Create naming conventions
   - Define coding standards
   - Establish review checklists
   - Document procedures

---

## Key Technologies

### Relational Databases
- PostgreSQL (Advanced)
- MySQL/MariaDB
- SQL Server
- Oracle

### NoSQL Databases
- MongoDB (Document)
- Redis (Key-Value)
- Cassandra (Wide-Column)
- Neo4j (Graph)

### Cloud Databases
- AWS RDS, Aurora, DynamoDB
- Azure SQL, Cosmos DB
- Google Cloud SQL, Spanner

### Tools
- Query analyzers
- Performance profilers
- Schema visualization
- Migration tools

---

## Deliverables

### Phase 1: Framework Definition
- [ ] Competency framework document
- [ ] Skill assessment rubric
- [ ] Learning path guide
- [ ] Technology matrix

### Phase 2: Knowledge Base
- [ ] Design patterns catalog
- [ ] Anti-patterns documentation
- [ ] Optimization techniques guide
- [ ] Security best practices

### Phase 3: Assessment Tools
- [ ] Schema review checklist
- [ ] Performance evaluation criteria
- [ ] Security audit checklist
- [ ] Documentation standards

### Phase 4: Training Materials
- [ ] Tutorial documents
- [ ] Reference architectures
- [ ] Example implementations
- [ ] Case studies

---

## Success Criteria

### Knowledge Coverage
- [ ] All core competencies documented
- [ ] Patterns catalog comprehensive
- [ ] Anti-patterns identified
- [ ] Best practices current

### Assessment Quality
- [ ] Clear evaluation criteria
- [ ] Objective measurements
- [ ] Actionable feedback
- [ ] Improvement tracking

### Practical Application
- [ ] Guidance is actionable
- [ ] Examples are realistic
- [ ] Recommendations are specific
- [ ] Materials are accessible

---

## File Type Location Rules

### Knowledge Base Structure
```
db-architect-skill/
├── SKILL.md                    # This file
├── competencies/
│   ├── core-skills.md          # Required competencies
│   ├── advanced-skills.md      # Senior-level skills
│   └── assessment-rubric.md    # Evaluation criteria
├── patterns/
│   ├── design-patterns.md      # Good patterns
│   ├── anti-patterns.md        # Patterns to avoid
│   └── decision-matrix.md      # When to use what
├── best-practices/
│   ├── schema-design.md        # Schema best practices
│   ├── query-optimization.md   # Query best practices
│   ├── security.md             # Security practices
│   └── scalability.md          # Scaling patterns
├── checklists/
│   ├── schema-review.md        # Schema review checklist
│   ├── performance-audit.md    # Performance checklist
│   └── security-audit.md       # Security checklist
├── references/
│   ├── naming-conventions.md   # Naming standards
│   ├── data-types.md           # Data type guide
│   └── index-strategies.md     # Indexing guide
└── training/
    ├── learning-path.md        # Skill development path
    ├── exercises/              # Practice exercises
    └── case-studies/           # Real-world examples
```

---

## Core Competency Framework

### Level 1: Foundation
```markdown
## Foundation Skills (Required for all DB work)

### SQL Proficiency
- [ ] SELECT with JOINs (INNER, LEFT, RIGHT, FULL)
- [ ] Aggregations (GROUP BY, HAVING)
- [ ] Subqueries and CTEs
- [ ] INSERT, UPDATE, DELETE operations
- [ ] Basic indexing concepts

### Data Modeling Basics
- [ ] Entity-Relationship diagrams
- [ ] Primary and foreign keys
- [ ] Basic normalization (1NF, 2NF, 3NF)
- [ ] One-to-one, one-to-many, many-to-many relationships
- [ ] Data types selection

### Database Operations
- [ ] Create tables and constraints
- [ ] Basic query writing
- [ ] Simple performance analysis
- [ ] Backup and restore basics
```

### Level 2: Intermediate
```markdown
## Intermediate Skills (For DB development)

### Advanced SQL
- [ ] Window functions
- [ ] Recursive CTEs
- [ ] Advanced aggregations
- [ ] Query optimization basics
- [ ] Execution plan reading

### Schema Design
- [ ] Denormalization strategies
- [ ] Surrogate vs natural keys
- [ ] Audit column patterns
- [ ] Soft delete patterns
- [ ] History/versioning tables

### Performance
- [ ] Index types and usage
- [ ] Query plan analysis
- [ ] Connection pooling
- [ ] Basic partitioning
- [ ] Caching strategies
```

### Level 3: Advanced
```markdown
## Advanced Skills (For DB architecture)

### Architecture Design
- [ ] Distributed database patterns
- [ ] Sharding strategies
- [ ] Replication configurations
- [ ] High availability design
- [ ] Disaster recovery planning

### Performance Mastery
- [ ] Advanced query optimization
- [ ] Partitioning strategies
- [ ] Memory tuning
- [ ] I/O optimization
- [ ] Lock management

### Security Architecture
- [ ] Row-level security
- [ ] Data encryption at rest
- [ ] Audit logging design
- [ ] Access control patterns
- [ ] Compliance requirements
```

---

## Design Pattern Catalog

### Structural Patterns

#### 1. Audit Trail Pattern
```sql
-- Purpose: Track all changes to sensitive data
-- When to use: Compliance requirements, debugging, history tracking

CREATE TABLE users (
    id UUID PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    -- ... other columns
    
    -- Audit columns
    created_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    created_by UUID REFERENCES users(id),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_by UUID REFERENCES users(id),
    version INTEGER NOT NULL DEFAULT 1
);

-- Trigger to auto-update audit fields
CREATE TRIGGER trg_users_audit
    BEFORE UPDATE ON users
    FOR EACH ROW
    EXECUTE FUNCTION fn_update_audit_fields();
```

#### 2. Soft Delete Pattern
```sql
-- Purpose: Mark records as deleted without physical removal
-- When to use: Need to recover data, audit requirements, referential integrity

CREATE TABLE orders (
    id UUID PRIMARY KEY,
    -- ... other columns
    
    deleted_at TIMESTAMPTZ,  -- NULL = active, timestamp = deleted
    deleted_by UUID REFERENCES users(id)
);

-- Always filter in queries
CREATE VIEW active_orders AS
SELECT * FROM orders WHERE deleted_at IS NULL;
```

#### 3. Type/Status Lookup Pattern
```sql
-- Purpose: Maintain controlled vocabulary for statuses/types
-- When to use: Limited set of valid values, need descriptions

CREATE TABLE order_status (
    code VARCHAR(20) PRIMARY KEY,  -- 'PENDING', 'SHIPPED', etc.
    name VARCHAR(100) NOT NULL,
    description TEXT,
    is_active BOOLEAN DEFAULT true,
    sort_order INTEGER
);

CREATE TABLE orders (
    id UUID PRIMARY KEY,
    status VARCHAR(20) NOT NULL REFERENCES order_status(code)
);
```

### Query Patterns

#### 1. Pagination Pattern
```sql
-- Purpose: Efficiently paginate large result sets
-- When to use: Any list/table display with many rows

-- Offset pagination (simple but slow for large offsets)
SELECT * FROM orders
ORDER BY created_at DESC
LIMIT 20 OFFSET 40;  -- Page 3

-- Keyset pagination (better for large datasets)
SELECT * FROM orders
WHERE created_at < '2024-01-15T10:00:00Z'  -- Last item from previous page
ORDER BY created_at DESC
LIMIT 20;
```

#### 2. Optimistic Locking Pattern
```sql
-- Purpose: Prevent lost updates in concurrent environments
-- When to use: Multiple users editing same records

-- Add version column
ALTER TABLE orders ADD COLUMN version INTEGER DEFAULT 1;

-- Update with version check
UPDATE orders
SET 
    status = 'SHIPPED',
    version = version + 1,
    updated_at = CURRENT_TIMESTAMP
WHERE id = $1 AND version = $2;  -- Expected version

-- Check if update succeeded (rows affected = 1)
-- If 0 rows, someone else updated - handle conflict
```

---

## Anti-Pattern Catalog

### Schema Anti-Patterns

#### 1. ❌ God Table
```sql
-- BAD: One table for everything
CREATE TABLE entities (
    id SERIAL PRIMARY KEY,
    entity_type VARCHAR(50),  -- 'user', 'order', 'product'
    field1 TEXT,
    field2 TEXT,
    -- ... 50 more generic fields
);

-- GOOD: Separate, focused tables
CREATE TABLE users (id, email, name, ...);
CREATE TABLE orders (id, user_id, total, ...);
CREATE TABLE products (id, name, price, ...);
```

#### 2. ❌ Entity-Attribute-Value (EAV) Overuse
```sql
-- BAD: Using EAV for core attributes
CREATE TABLE user_attributes (
    user_id INTEGER,
    attribute_name VARCHAR(100),
    attribute_value TEXT
);
-- Query: "SELECT email" requires pivot or multiple rows

-- GOOD: Proper columns
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    email VARCHAR(255),
    name VARCHAR(100)
);
-- EAV is okay for truly dynamic, user-defined attributes
```

#### 3. ❌ Storing Comma-Separated Values
```sql
-- BAD: Multiple values in one column
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    roles VARCHAR(255)  -- 'admin,user,editor'
);

-- GOOD: Proper relationship table
CREATE TABLE user_roles (
    user_id INTEGER REFERENCES users(id),
    role_id INTEGER REFERENCES roles(id),
    PRIMARY KEY (user_id, role_id)
);
```

### Query Anti-Patterns

#### 1. ❌ SELECT *
```sql
-- BAD: Fetching all columns
SELECT * FROM orders WHERE user_id = 1;

-- GOOD: Explicit columns needed
SELECT id, status, total, created_at 
FROM orders 
WHERE user_id = 1;
```

#### 2. ❌ N+1 Query Problem
```sql
-- BAD: One query per order
FOR order IN (SELECT * FROM orders):
    SELECT * FROM order_items WHERE order_id = order.id;

-- GOOD: Single query with JOIN
SELECT o.*, oi.*
FROM orders o
LEFT JOIN order_items oi ON o.id = oi.order_id;

-- Or use subquery
SELECT o.*,
    (SELECT json_agg(oi) FROM order_items oi WHERE oi.order_id = o.id) as items
FROM orders o;
```

---

## Schema Review Checklist

```markdown
## Schema Review Checklist

### Naming Conventions
- [ ] Tables: plural, snake_case (e.g., `users`, `order_items`)
- [ ] Columns: snake_case (e.g., `created_at`, `user_id`)
- [ ] Primary keys: `id` or `table_singular_id`
- [ ] Foreign keys: `referenced_table_singular_id`
- [ ] Indexes: `idx_table_columns`
- [ ] Constraints: `table_column_type` (e.g., `uq_users_email`)

### Table Design
- [ ] Every table has a primary key
- [ ] Foreign keys have indexes
- [ ] Appropriate data types selected
- [ ] NOT NULL constraints where appropriate
- [ ] Default values defined where sensible
- [ ] Audit columns present (created_at, updated_at)

### Normalization
- [ ] 3NF achieved or strategic denormalization documented
- [ ] No repeating groups
- [ ] No transitive dependencies
- [ ] Calculated values not stored (or documented reason)

### Relationships
- [ ] All relationships defined with foreign keys
- [ ] ON DELETE/UPDATE actions specified
- [ ] Many-to-many uses junction tables
- [ ] No orphan records possible

### Performance Considerations
- [ ] Indexes on frequently queried columns
- [ ] Composite indexes for common queries
- [ ] Partitioning considered for large tables
- [ ] No over-indexing

### Security
- [ ] Sensitive data identified
- [ ] Encryption plan for sensitive columns
- [ ] Access control strategy defined
- [ ] Audit requirements met

### Documentation
- [ ] All tables documented
- [ ] All columns have descriptions
- [ ] Relationships documented
- [ ] Indexes explained
- [ ] Data dictionary complete
```

---

## Integration Points

### Coordinates With
- **DB Architect**: Applies skills in practice
- **Backend Developer**: SQL guidance, query review
- **Data Migration**: Migration pattern guidance
- **QA Testing**: Database testing strategies
- **Documentation**: DB documentation standards

### Provides To
- Competency assessment frameworks
- Design pattern recommendations
- Review checklists
- Training materials
- Best practice guidance

---

## Assessment Rubric

### Schema Design (0-10 points)
| Score | Criteria |
|-------|----------|
| 9-10 | Optimal design, all best practices followed |
| 7-8 | Good design, minor improvements possible |
| 5-6 | Acceptable, some patterns missing |
| 3-4 | Significant issues, requires rework |
| 0-2 | Major problems, fundamental issues |

### Query Quality (0-10 points)
| Score | Criteria |
|-------|----------|
| 9-10 | Highly optimized, efficient patterns |
| 7-8 | Good performance, minor optimizations possible |
| 5-6 | Acceptable, some N+1 or inefficiencies |
| 3-4 | Poor performance, needs rewrite |
| 0-2 | Critical issues, blocking performance |

### Documentation (0-10 points)
| Score | Criteria |
|-------|----------|
| 9-10 | Complete, clear, up-to-date |
| 7-8 | Good coverage, minor gaps |
| 5-6 | Basic documentation present |
| 3-4 | Incomplete, outdated |
| 0-2 | Missing or severely lacking |

---

## Anti-Patterns to Avoid

1. **Dogmatic Normalization**: Know when to denormalize
2. **Ignoring Query Patterns**: Design for actual usage
3. **Over-Engineering**: Start simple, optimize when needed
4. **Under-Documenting**: Document all design decisions
5. **Skipping Reviews**: Always peer review schemas
6. **Premature Optimization**: Profile first, then optimize
7. **Ignoring Maintenance**: Consider long-term operations
8. **One-Size-Fits-All**: Choose right tool for the job
9. **Ignoring Security**: Security from the start
10. **No Versioning**: Version control all schema changes
