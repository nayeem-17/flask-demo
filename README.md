# Project documentation

## Add this to `.env` file

```bash
# Environment variables file (for development)
FLASK_ENV=development
FLASK_APP=manage.py
FLASK_RUN_PORT=5000
```

### Flask Migrations with Flask-Migrate:

Flask-Migrate is a powerful extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
Below is a comprehensive guide to using Flask-Migrate with best practices to ensure smooth database management.

#### 1. **Installation and Setup**

First, you need to install the necessary packages:

```bash
pip install Flask-Migrate psycopg2-binary
```

#### 2. **Creating and Running Migrations**

- **Initialize Migrations**:

  Before creating any migrations, initialize the migration environment:

  ```bash
  flask db init
  ```

  This creates a `migrations/` directory in your project with the necessary files to manage migrations.

- **Create a New Migration**:

  Every time you make changes to your models, you need to create a new migration:

  ```bash
  flask db migrate -m "Describe your changes"
  ```

  This command will detect changes in your models and generate a migration script.

- **Apply Migrations**:

  To apply the migrations to your database, use:

  ```bash
  flask db upgrade
  ```

  This will apply the changes defined in your migration scripts to your database schema.

- **Downgrade Migrations**:

  If you need to revert a migration, you can downgrade to the previous state:

  ```bash
  flask db downgrade
  ```

  This reverts the most recent migration, useful if something goes wrong.

#### 3. **Best Practices**

- **Version Control**:

  Always commit your migration scripts to version control. This ensures that your team can apply the same migrations and
  keep the database schema consistent across different environments.

- **Descriptive Migration Messages**:

  When running `flask db migrate`, always include a descriptive message with the `-m` flag that clearly states what the
  migration does. For example:

  ```bash
  flask db migrate -m "Add email field to User model"
  ```

  This helps track changes easily, especially when revisiting older migrations.

- **Review Migration Scripts**:

  Before running `flask db upgrade`, review the generated migration script. Alembic may not always detect changes
  correctly, especially with complex migrations, so it's good practice to manually verify the migration file.

- **Maintain Data Integrity**:

  Be careful when making changes that could affect existing data. Always back up your database before running
  migrations, particularly in production environments.

- **Separate Migration Operations**:

  For complex operations (e.g., renaming columns, dropping columns), separate them into individual migrations and handle
  data transformation explicitly. This reduces the risk of data loss or corruption.

- **Use Alembic Commands**:

  You can manually create and edit migration scripts using Alembic commands like:

  ```bash
  flask db revision --autogenerate -m "Your migration message"
  ```

  This allows more granular control over migration scripts.

- **Environment-Specific Configurations**:

  Use different configuration files for development, testing, and production environments. Make sure that
  `SQLALCHEMY_DATABASE_URI` is set correctly for each environment.

#### 4. **Deployment Considerations**

- **Automate Migrations**:

  In a CI/CD pipeline, automate the migration process to ensure that every deployment applies the latest database
  schema. For instance:

  ```bash
  flask db upgrade
  ```

  This command can be part of your deployment scripts to ensure your database is always up-to-date.

- **Production Safety**:

  Never run migrations directly on the production database without thoroughly testing them in a staging environment.
  Consider using a zero-downtime deployment strategy if your application is sensitive to downtime.

#### 5. **Rollback Strategy**

In case of a failed migration or unexpected issues, ensure that you have a rollback strategy. This involves:

- Backing up the database before running migrations.
- Testing migrations in a staging environment.
- Using `flask db downgrade` to rollback changes if needed.

#### 6. **Handling Schema Changes**

- **Adding New Columns**:

  Ensure that new columns allow `NULL` if you are adding them to existing tables with data, then update the data and
  apply a migration to make the column `NOT NULL`.

- **Renaming Columns**:

  Renaming columns may require special attention as Alembic might not detect this automatically. You may need to
  manually edit the migration script to handle the renaming process correctly.

- **Dropping Columns**:

  If dropping a column, ensure it’s not being used anywhere in the application before the migration is applied.

#### 7. **Testing Migrations**

Always test your migrations in a development or staging environment before applying them to production. This can help
you identify issues and fix them before they affect the live system.
