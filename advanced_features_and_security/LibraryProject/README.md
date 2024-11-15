**This documentation explains how the permissions of the bookshelf app and the groups existing within the app.**

## Model Permissions
- `can_view`: Allows a user to view articles.
- `can_create`: Allows a user to create new articles.
- `can_edit`: Allows a user to edit existing articles.
- `can_delete`: Allows a user to delete articles.

## Groups
- Viewers: Only have `can_view` permission.
- Editors: Have `can_create` and `can_edit` permissions.
- Admins: Have all permissions.

## Views
- Views for creating, editing, deleting, and viewing articles check for the appropriate permissions using `@permission_required` decorator.
