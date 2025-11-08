---
title: "Verify users cannot modify system hooks"
source: ""
---

# Verify users cannot modify system hooks
sudo chown root:root /etc/windsurf/hooks.json
sudo chmod 644 /etc/windsurf/hooks.json
```

<Note>
  **Important**: System-level hooks are entirely managed by your IT or security team. Windsurf does not deploy or manage files at system-level paths. Ensure your internal teams handle deployment, updates, and compliance according to your organization's policies.
</Note>

### Workspace Hooks for Team Projects

For project-specific conventions, teams can use workspace-level hooks in version control:

```bash  theme={null}

---

← Previous: [Have a developer trigger the relevant Cascade action](./have-a-developer-trigger-the-relevant-cascade-action.md) | [Index](./index.md) | Next: [Add to your repository](./add-to-your-repository.md) →