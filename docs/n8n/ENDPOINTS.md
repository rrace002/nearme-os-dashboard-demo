# n8n Public API endpoint catalog

Generated from live OpenAPI specs for project documentation.

- Auth header: `X-N8N-API-KEY`
- Base path: `/api/v1`
- Official docs: https://docs.n8n.io/connect/n8n-api/
- Official OpenAPI (n8n Cloud internal): https://internal.users.n8n.cloud/api/v1/openapi.yml
- Our instance docs: https://n8n.racecs.com/api/v1/docs/
- Our instance OpenAPI: https://n8n.racecs.com/api/v1/openapi.yml

## Instance comparison

| Source | Version | Paths | Operations | Tags |
| --- | --- | --- | --- | --- |
| n8n.racecs.com | 1.1.1 | 26 | 41 | 9 |
| internal.users.n8n.cloud | 1.1.1 | 81 | 131 | 25 |

Our RaceCS instance currently publishes the older public-API surface (workflows, executions, credentials, users, tags, variables, projects, audit, source-control). The n8n Cloud spec adds data tables, packages, folders, git connections, roles, SSO/LDAP/OTEL settings, evaluations, insights, and more.

## n8n.racecs.com operations (41)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `POST` | `/audit` | Audit | Generate an audit |
| `POST` | `/credentials` | Credential | Create a credential |
| `GET` | `/credentials/schema/{credentialTypeName}` | Credential | Show credential data schema |
| `DELETE` | `/credentials/{id}` | Credential | Delete credential by ID |
| `PUT` | `/credentials/{id}/transfer` | Credential | Transfer a credential to another project. |
| `GET` | `/executions` | Execution | Retrieve all executions |
| `DELETE` | `/executions/{id}` | Execution | Delete an execution |
| `GET` | `/executions/{id}` | Execution | Retrieve an execution |
| `POST` | `/executions/{id}/retry` | Execution | Retry an execution |
| `GET` | `/projects` | Projects | Retrieve projects |
| `POST` | `/projects` | Projects | Create a project |
| `DELETE` | `/projects/{projectId}` | Projects | Delete a project |
| `PUT` | `/projects/{projectId}` | Projects | Update a project |
| `POST` | `/projects/{projectId}/users` | Projects | Add one or more users to a project |
| `DELETE` | `/projects/{projectId}/users/{userId}` | Projects | Delete a user from a project |
| `PATCH` | `/projects/{projectId}/users/{userId}` | Projects | Change a user's role in a project |
| `POST` | `/source-control/pull` | SourceControl | Pull changes from the remote repository |
| `GET` | `/tags` | Tags | Retrieve all tags |
| `POST` | `/tags` | Tags | Create a tag |
| `DELETE` | `/tags/{id}` | Tags | Delete a tag |
| `GET` | `/tags/{id}` | Tags | Retrieves a tag |
| `PUT` | `/tags/{id}` | Tags | Update a tag |
| `GET` | `/users` | User | Retrieve all users |
| `POST` | `/users` | User | Create multiple users |
| `DELETE` | `/users/{id}` | User | Delete a user |
| `GET` | `/users/{id}` | User | Get user by ID/Email |
| `PATCH` | `/users/{id}/role` | User | Change a user's global role |
| `GET` | `/variables` | Variables | Retrieve variables |
| `POST` | `/variables` | Variables | Create a variable |
| `DELETE` | `/variables/{id}` | Variables | Delete a variable |
| `PUT` | `/variables/{id}` | Variables | Update a variable |
| `GET` | `/workflows` | Workflow | Retrieve all workflows |
| `POST` | `/workflows` | Workflow | Create a workflow |
| `DELETE` | `/workflows/{id}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{id}` | Workflow | Retrieves a workflow |
| `PUT` | `/workflows/{id}` | Workflow | Update a workflow |
| `POST` | `/workflows/{id}/activate` | Workflow | Activate a workflow |
| `POST` | `/workflows/{id}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{id}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{id}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{id}/transfer` | Workflow | Transfer a workflow to another project. |

## n8n Cloud operations (131)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `POST` | `/audit` | Audit | Generate an audit |
| `GET` | `/community-packages` | CommunityPackage | List installed community packages |
| `POST` | `/community-packages` | CommunityPackage | Install a community package |
| `DELETE` | `/community-packages/{name}` | CommunityPackage | Uninstall a community package |
| `PATCH` | `/community-packages/{name}` | CommunityPackage | Update a community package |
| `GET` | `/credentials` | Credential | List credentials |
| `POST` | `/credentials` | Credential | Create a credential |
| `GET` | `/credentials/schema/{credentialTypeName}` | Credential | Show credential data schema |
| `DELETE` | `/credentials/{id}` | Credential | Delete credential by ID |
| `GET` | `/credentials/{id}` | Credential | Get credential by ID |
| `PATCH` | `/credentials/{id}` | Credential | Update credential by ID |
| `POST` | `/credentials/{id}/test` | Credential | Test credential by ID |
| `PUT` | `/credentials/{id}/transfer` | Credential | Transfer a credential to another project. |
| `GET` | `/data-tables` | DataTable | List all data tables |
| `POST` | `/data-tables` | DataTable | Create a new data table |
| `DELETE` | `/data-tables/{dataTableId}` | DataTable | Delete a data table |
| `GET` | `/data-tables/{dataTableId}` | DataTable | Get a data table |
| `PATCH` | `/data-tables/{dataTableId}` | DataTable | Update a data table |
| `GET` | `/data-tables/{dataTableId}/columns` | DataTable | List columns of a data table |
| `POST` | `/data-tables/{dataTableId}/columns` | DataTable | Add a column to a data table |
| `DELETE` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Delete a column |
| `PATCH` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Update a column |
| `GET` | `/data-tables/{dataTableId}/rows` | DataTable | Retrieve rows from a data table |
| `POST` | `/data-tables/{dataTableId}/rows` | DataTable | Insert rows into a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/clear` | DataTable | Clear all rows from a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/delete` | DataTable | Delete rows from a data table |
| `PATCH` | `/data-tables/{dataTableId}/rows/update` | DataTable | Update rows in a data table |
| `POST` | `/data-tables/{dataTableId}/rows/upsert` | DataTable | Upsert a row in a data table |
| `GET` | `/discover` | Discover | Discover available API capabilities |
| `GET` | `/workflows/{id}/test-runs` | Evaluation | Retrieve test runs |
| `POST` | `/workflows/{id}/test-runs` | Evaluation | Trigger a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}` | Evaluation | Retrieve a test run |
| `POST` | `/workflows/{id}/test-runs/{runId}/cancel` | Evaluation | Cancel a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}/test-cases` | Evaluation | Retrieve test run cases |
| `GET` | `/executions` | Execution | Retrieve all executions |
| `POST` | `/executions/stop` | Execution | Stop multiple executions |
| `DELETE` | `/executions/{id}` | Execution | Delete an execution |
| `GET` | `/executions/{id}` | Execution | Retrieve an execution |
| `POST` | `/executions/{id}/retry` | Execution | Retry an execution |
| `POST` | `/executions/{id}/stop` | Execution | Stop an execution |
| `GET` | `/executions/{id}/tags` | Execution | Get execution tags |
| `PUT` | `/executions/{id}/tags` | Execution | Update tags of an execution |
| `GET` | `/projects/{projectId}/folders` | Folders | Retrieve folders |
| `POST` | `/projects/{projectId}/folders` | Folders | Create a folder |
| `DELETE` | `/projects/{projectId}/folders/{folderId}` | Folders | Delete a folder |
| `GET` | `/projects/{projectId}/folders/{folderId}` | Folders | Get folder details |
| `PATCH` | `/projects/{projectId}/folders/{folderId}` | Folders | Update a folder |
| `GET` | `/git-connections` | GitConnections | List Git connections |
| `POST` | `/git-connections` | GitConnections | Create a Git connection |
| `DELETE` | `/git-connections/{id}` | GitConnections | Delete a Git connection |
| `GET` | `/git-connections/{id}` | GitConnections | Retrieve a Git connection |
| `PUT` | `/git-connections/{id}` | GitConnections | Update a Git connection |
| `POST` | `/git-connections/{id}/clone` | GitConnections | Clone a Git connection |
| `POST` | `/git-connections/{id}/disconnect` | GitConnections | Disconnect a Git connection |
| `GET` | `/git-connections/{id}/projects` | GitConnections | List projects added to a Git connection |
| `DELETE` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Remove a project from a Git connection |
| `POST` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Add a project to a Git connection |
| `POST` | `/git-connections/{id}/pull` | GitConnections | Import all projects from a Git connection working copy |
| `POST` | `/git-connections/{id}/push` | GitConnections | Push all team projects to a Git connection |
| `GET` | `/insights/summary` | Insights | Retrieve insights summary |
| `GET` | `/settings/log-streaming/destinations` | LogStreaming | List log streaming destinations |
| `POST` | `/settings/log-streaming/destinations` | LogStreaming | Create a log streaming destination |
| `DELETE` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Delete a log streaming destination |
| `GET` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Retrieve a log streaming destination |
| `PUT` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Update a log streaming destination |
| `POST` | `/settings/log-streaming/destinations/{id}/test` | LogStreaming | Send a test message to a log streaming destination |
| `GET` | `/settings/log-streaming/event-types` | LogStreaming | List streamable event types |
| `POST` | `/n8n-packages/export` | N8nPackage | Beta: Export workflows, folders, or projects as an n8n package |
| `POST` | `/n8n-packages/import` | N8nPackage | Beta: Import an n8n package into a project |
| `GET` | `/projects` | Projects | Retrieve projects |
| `POST` | `/projects` | Projects | Create a project |
| `DELETE` | `/projects/{projectId}` | Projects | Delete a project |
| `PUT` | `/projects/{projectId}` | Projects | Update a project |
| `GET` | `/projects/{projectId}/users` | Projects | List project members |
| `POST` | `/projects/{projectId}/users` | Projects | Add one or more users to a project |
| `DELETE` | `/projects/{projectId}/users/{userId}` | Projects | Delete a user from a project |
| `PATCH` | `/projects/{projectId}/users/{userId}` | Projects | Change a user's role in a project |
| `GET` | `/roles` | Role | Retrieve all roles |
| `POST` | `/roles` | Role | Create a custom role |
| `DELETE` | `/roles/{slug}` | Role | Delete a custom role |
| `GET` | `/roles/{slug}` | Role | Retrieve a role |
| `PUT` | `/roles/{slug}` | Role | Update a custom role |
| `GET` | `/role-mapping-rules` | RoleMappingRule | Retrieve role-mapping rules |
| `POST` | `/role-mapping-rules` | RoleMappingRule | Create a role-mapping rule |
| `DELETE` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Delete a role-mapping rule |
| `PATCH` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Update a role-mapping rule |
| `POST` | `/role-mapping-rules/{roleMappingRuleId}/move` | RoleMappingRule | Move a role-mapping rule |
| `GET` | `/settings/security-policy` | SecurityPolicy | Retrieve the security policy |
| `PUT` | `/settings/security-policy` | SecurityPolicy | Set the security policy |
| `GET` | `/settings/ldap` | SettingsLdap | Retrieve the LDAP configuration |
| `PUT` | `/settings/ldap` | SettingsLdap | Set the LDAP configuration |
| `GET` | `/settings/ldap/sync` | SettingsLdap | Retrieve LDAP synchronization history |
| `POST` | `/settings/ldap/sync` | SettingsLdap | Trigger an LDAP synchronization |
| `GET` | `/settings/otel` | SettingsOtel | Retrieve the OpenTelemetry configuration |
| `PUT` | `/settings/otel` | SettingsOtel | Set the OpenTelemetry configuration |
| `POST` | `/settings/otel/test-trace` | SettingsOtel | Test the connection to an OTLP collector |
| `GET` | `/settings/sso/oidc` | SettingsSsoOidc | Retrieve the OIDC SSO configuration |
| `PUT` | `/settings/sso/oidc` | SettingsSsoOidc | Set the OIDC SSO configuration |
| `GET` | `/settings/sso/saml` | SettingsSsoSaml | Retrieve the SAML SSO configuration |
| `PUT` | `/settings/sso/saml` | SettingsSsoSaml | Set the SAML SSO configuration |
| `POST` | `/source-control/pull` | SourceControl | Pull changes from the remote repository |
| `GET` | `/tags` | Tags | Retrieve all tags |
| `POST` | `/tags` | Tags | Create a tag |
| `DELETE` | `/tags/{id}` | Tags | Delete a tag |
| `GET` | `/tags/{id}` | Tags | Retrieves a tag |
| `PUT` | `/tags/{id}` | Tags | Update a tag |
| `GET` | `/users` | User | Retrieve all users |
| `POST` | `/users` | User | Create multiple users |
| `DELETE` | `/users/{id}` | User | Delete a user |
| `GET` | `/users/{id}` | User | Get user by ID/Email |
| `PATCH` | `/users/{id}/role` | User | Change a user's global role |
| `GET` | `/variables` | Variables | Retrieve variables |
| `POST` | `/variables` | Variables | Create a variable |
| `DELETE` | `/variables/{id}` | Variables | Delete a variable |
| `PUT` | `/variables/{id}` | Variables | Update a variable |
| `GET` | `/workflows` | Workflow | Retrieve all workflows |
| `POST` | `/workflows` | Workflow | Create a workflow |
| `GET` | `/workflows/{id}/{versionId}` | Workflow | Retrieves a specific version of a workflow |
| `DELETE` | `/workflows/{workflowId}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{workflowId}` | Workflow | Retrieve a workflow |
| `PUT` | `/workflows/{workflowId}` | Workflow | Update a workflow |
| `POST` | `/workflows/{workflowId}/activate` | Workflow | Publish a workflow |
| `POST` | `/workflows/{workflowId}/archive` | Workflow | Archive a workflow |
| `POST` | `/workflows/{workflowId}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{workflowId}/history` | Workflow | Retrieve workflow version history |
| `POST` | `/workflows/{workflowId}/publish` | Workflow | Publish a workflow |
| `GET` | `/workflows/{workflowId}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{workflowId}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{workflowId}/transfer` | Workflow | Transfer a workflow to another project |
| `POST` | `/workflows/{workflowId}/unarchive` | Workflow | Unarchive a workflow |
| `POST` | `/workflows/{workflowId}/unpublish` | Workflow | Unpublish a workflow |

## Present on Cloud spec only (98)

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `GET` | `/community-packages` | CommunityPackage | List installed community packages |
| `POST` | `/community-packages` | CommunityPackage | Install a community package |
| `DELETE` | `/community-packages/{name}` | CommunityPackage | Uninstall a community package |
| `PATCH` | `/community-packages/{name}` | CommunityPackage | Update a community package |
| `GET` | `/credentials` | Credential | List credentials |
| `GET` | `/credentials/{id}` | Credential | Get credential by ID |
| `PATCH` | `/credentials/{id}` | Credential | Update credential by ID |
| `POST` | `/credentials/{id}/test` | Credential | Test credential by ID |
| `GET` | `/data-tables` | DataTable | List all data tables |
| `POST` | `/data-tables` | DataTable | Create a new data table |
| `DELETE` | `/data-tables/{dataTableId}` | DataTable | Delete a data table |
| `GET` | `/data-tables/{dataTableId}` | DataTable | Get a data table |
| `PATCH` | `/data-tables/{dataTableId}` | DataTable | Update a data table |
| `GET` | `/data-tables/{dataTableId}/columns` | DataTable | List columns of a data table |
| `POST` | `/data-tables/{dataTableId}/columns` | DataTable | Add a column to a data table |
| `DELETE` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Delete a column |
| `PATCH` | `/data-tables/{dataTableId}/columns/{columnId}` | DataTable | Update a column |
| `GET` | `/data-tables/{dataTableId}/rows` | DataTable | Retrieve rows from a data table |
| `POST` | `/data-tables/{dataTableId}/rows` | DataTable | Insert rows into a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/clear` | DataTable | Clear all rows from a data table |
| `DELETE` | `/data-tables/{dataTableId}/rows/delete` | DataTable | Delete rows from a data table |
| `PATCH` | `/data-tables/{dataTableId}/rows/update` | DataTable | Update rows in a data table |
| `POST` | `/data-tables/{dataTableId}/rows/upsert` | DataTable | Upsert a row in a data table |
| `GET` | `/discover` | Discover | Discover available API capabilities |
| `GET` | `/workflows/{id}/test-runs` | Evaluation | Retrieve test runs |
| `POST` | `/workflows/{id}/test-runs` | Evaluation | Trigger a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}` | Evaluation | Retrieve a test run |
| `POST` | `/workflows/{id}/test-runs/{runId}/cancel` | Evaluation | Cancel a test run |
| `GET` | `/workflows/{id}/test-runs/{runId}/test-cases` | Evaluation | Retrieve test run cases |
| `POST` | `/executions/stop` | Execution | Stop multiple executions |
| `POST` | `/executions/{id}/stop` | Execution | Stop an execution |
| `GET` | `/executions/{id}/tags` | Execution | Get execution tags |
| `PUT` | `/executions/{id}/tags` | Execution | Update tags of an execution |
| `GET` | `/projects/{projectId}/folders` | Folders | Retrieve folders |
| `POST` | `/projects/{projectId}/folders` | Folders | Create a folder |
| `DELETE` | `/projects/{projectId}/folders/{folderId}` | Folders | Delete a folder |
| `GET` | `/projects/{projectId}/folders/{folderId}` | Folders | Get folder details |
| `PATCH` | `/projects/{projectId}/folders/{folderId}` | Folders | Update a folder |
| `GET` | `/git-connections` | GitConnections | List Git connections |
| `POST` | `/git-connections` | GitConnections | Create a Git connection |
| `DELETE` | `/git-connections/{id}` | GitConnections | Delete a Git connection |
| `GET` | `/git-connections/{id}` | GitConnections | Retrieve a Git connection |
| `PUT` | `/git-connections/{id}` | GitConnections | Update a Git connection |
| `POST` | `/git-connections/{id}/clone` | GitConnections | Clone a Git connection |
| `POST` | `/git-connections/{id}/disconnect` | GitConnections | Disconnect a Git connection |
| `GET` | `/git-connections/{id}/projects` | GitConnections | List projects added to a Git connection |
| `DELETE` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Remove a project from a Git connection |
| `POST` | `/git-connections/{id}/projects/{projectId}` | GitConnections | Add a project to a Git connection |
| `POST` | `/git-connections/{id}/pull` | GitConnections | Import all projects from a Git connection working copy |
| `POST` | `/git-connections/{id}/push` | GitConnections | Push all team projects to a Git connection |
| `GET` | `/insights/summary` | Insights | Retrieve insights summary |
| `GET` | `/settings/log-streaming/destinations` | LogStreaming | List log streaming destinations |
| `POST` | `/settings/log-streaming/destinations` | LogStreaming | Create a log streaming destination |
| `DELETE` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Delete a log streaming destination |
| `GET` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Retrieve a log streaming destination |
| `PUT` | `/settings/log-streaming/destinations/{id}` | LogStreaming | Update a log streaming destination |
| `POST` | `/settings/log-streaming/destinations/{id}/test` | LogStreaming | Send a test message to a log streaming destination |
| `GET` | `/settings/log-streaming/event-types` | LogStreaming | List streamable event types |
| `POST` | `/n8n-packages/export` | N8nPackage | Beta: Export workflows, folders, or projects as an n8n package |
| `POST` | `/n8n-packages/import` | N8nPackage | Beta: Import an n8n package into a project |
| `GET` | `/projects/{projectId}/users` | Projects | List project members |
| `GET` | `/roles` | Role | Retrieve all roles |
| `POST` | `/roles` | Role | Create a custom role |
| `DELETE` | `/roles/{slug}` | Role | Delete a custom role |
| `GET` | `/roles/{slug}` | Role | Retrieve a role |
| `PUT` | `/roles/{slug}` | Role | Update a custom role |
| `GET` | `/role-mapping-rules` | RoleMappingRule | Retrieve role-mapping rules |
| `POST` | `/role-mapping-rules` | RoleMappingRule | Create a role-mapping rule |
| `DELETE` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Delete a role-mapping rule |
| `PATCH` | `/role-mapping-rules/{roleMappingRuleId}` | RoleMappingRule | Update a role-mapping rule |
| `POST` | `/role-mapping-rules/{roleMappingRuleId}/move` | RoleMappingRule | Move a role-mapping rule |
| `GET` | `/settings/security-policy` | SecurityPolicy | Retrieve the security policy |
| `PUT` | `/settings/security-policy` | SecurityPolicy | Set the security policy |
| `GET` | `/settings/ldap` | SettingsLdap | Retrieve the LDAP configuration |
| `PUT` | `/settings/ldap` | SettingsLdap | Set the LDAP configuration |
| `GET` | `/settings/ldap/sync` | SettingsLdap | Retrieve LDAP synchronization history |
| `POST` | `/settings/ldap/sync` | SettingsLdap | Trigger an LDAP synchronization |
| `GET` | `/settings/otel` | SettingsOtel | Retrieve the OpenTelemetry configuration |
| `PUT` | `/settings/otel` | SettingsOtel | Set the OpenTelemetry configuration |
| `POST` | `/settings/otel/test-trace` | SettingsOtel | Test the connection to an OTLP collector |
| `GET` | `/settings/sso/oidc` | SettingsSsoOidc | Retrieve the OIDC SSO configuration |
| `PUT` | `/settings/sso/oidc` | SettingsSsoOidc | Set the OIDC SSO configuration |
| `GET` | `/settings/sso/saml` | SettingsSsoSaml | Retrieve the SAML SSO configuration |
| `PUT` | `/settings/sso/saml` | SettingsSsoSaml | Set the SAML SSO configuration |
| `GET` | `/workflows/{id}/{versionId}` | Workflow | Retrieves a specific version of a workflow |
| `DELETE` | `/workflows/{workflowId}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{workflowId}` | Workflow | Retrieve a workflow |
| `PUT` | `/workflows/{workflowId}` | Workflow | Update a workflow |
| `POST` | `/workflows/{workflowId}/activate` | Workflow | Publish a workflow |
| `POST` | `/workflows/{workflowId}/archive` | Workflow | Archive a workflow |
| `POST` | `/workflows/{workflowId}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{workflowId}/history` | Workflow | Retrieve workflow version history |
| `POST` | `/workflows/{workflowId}/publish` | Workflow | Publish a workflow |
| `GET` | `/workflows/{workflowId}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{workflowId}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{workflowId}/transfer` | Workflow | Transfer a workflow to another project |
| `POST` | `/workflows/{workflowId}/unarchive` | Workflow | Unarchive a workflow |
| `POST` | `/workflows/{workflowId}/unpublish` | Workflow | Unpublish a workflow |

## Present on RaceCS spec only (8)

These are the same workflow routes using `{id}` instead of `{workflowId}`.

| Method | Path | Tag | Summary |
| --- | --- | --- | --- |
| `DELETE` | `/workflows/{id}` | Workflow | Delete a workflow |
| `GET` | `/workflows/{id}` | Workflow | Retrieves a workflow |
| `PUT` | `/workflows/{id}` | Workflow | Update a workflow |
| `POST` | `/workflows/{id}/activate` | Workflow | Activate a workflow |
| `POST` | `/workflows/{id}/deactivate` | Workflow | Deactivate a workflow |
| `GET` | `/workflows/{id}/tags` | Workflow | Get workflow tags |
| `PUT` | `/workflows/{id}/tags` | Workflow | Update tags of a workflow |
| `PUT` | `/workflows/{id}/transfer` | Workflow | Transfer a workflow to another project. |
