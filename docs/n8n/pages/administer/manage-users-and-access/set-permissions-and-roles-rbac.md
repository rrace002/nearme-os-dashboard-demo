> For the complete documentation index, see [llms.txt](https://docs.n8n.io/llms.txt). Markdown versions of documentation pages are available by appending `.md` to page URLs; this page is available as [Markdown](https://docs.n8n.io/administer/manage-users-and-access/set-permissions-and-roles-rbac.md).

# Set permissions and roles (RBAC)

{% hint style="info" %}
**Feature availability**

Project roles are available on:

* **n8n Cloud:** All plans
* **Self-hosted:** Registered Community, Business, Enterprise

Custom roles (instance and project) are available on:

* **n8n Cloud:** Enterprise
* **Self-hosted:** Enterprise
  {% endhint %}

RBAC in n8n lets you control access at two levels:

* **Instance roles**: determine what a user can do across the entire instance. Built-in instance roles are Owner, Admin, and Member. You can also create custom instance roles for more granular control. Refer to [Instance roles](/administer/manage-users-and-access/understand-instance-roles.md).
* **Project roles**: determine what a user can do within a specific project. You group workflows and credentials into projects, and a user can have different project roles in different projects. Refer to [See available roles](/administer/manage-users-and-access/set-permissions-and-roles-rbac/see-available-roles.md).

This section provides guidance on setting up and using RBAC in n8n.
