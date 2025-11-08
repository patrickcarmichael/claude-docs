---
title: "Format based on file extension"
source: ""
---

# Format based on file extension
if [[ "$file_path" == *.py ]]; then
    black "$file_path" 2>&1
    echo "Formatted Python file: $file_path"
elif [[ "$file_path" == *.js ]] || [[ "$file_path" == *.ts ]]; then
    prettier --write "$file_path" 2>&1
    echo "Formatted JS/TS file: $file_path"
elif [[ "$file_path" == *.go ]]; then
    gofmt -w "$file_path" 2>&1
    echo "Formatted Go file: $file_path"
fi

exit 0
```

This hook automatically runs the appropriate formatter based on the file type after each edit.

## Best Practices

### Security

<Warning>
  **Use Cascade Hooks at Your Own Risk**: Hooks execute shell commands automatically with your user account's full permissions. You are entirely responsible for the code you configure. Poorly designed or malicious hooks can modify files, delete data, expose credentials, or compromise your system.
</Warning>

* **Validate all inputs**: Never trust the input JSON without validation, especially for file paths and commands.
* **Use absolute paths**: Always use absolute paths in your hook configurations to avoid ambiguity.
* **Protect sensitive data**: Avoid logging sensitive information like API keys or credentials.
* **Review permissions**: Ensure your hook scripts have appropriate file system permissions.
* **Audit before deployment**: Review every hook command and script before adding to your configuration.
* **Test in isolation**: Run hooks in a test environment before enabling them on your primary development machine.

### Performance Considerations

* **Keep hooks fast**: Slow hooks will impact Cascade's responsiveness. Aim for sub-100ms execution times.
* **Use async operations**: For non-blocking hooks, consider logging to a queue or database asynchronously.
* **Filter early**: Check the action type at the start of your script to avoid unnecessary processing.

### Error Handling

* **Always validate JSON**: Use try-catch blocks to handle malformed input gracefully.
* **Log errors properly**: Write errors to `stderr` so they're visible when `show_output` is enabled.
* **Fail safely**: If your hook encounters an error, consider whether it should block the action or allow it to proceed.

### Testing Your Hooks

1. **Start with logging**: Begin by implementing a simple logging hook to understand the data flow.
2. **Use `show_output: true`**: Enable output during development to see what your hooks are doing.
3. **Test blocking behavior**: Verify that exit code 2 properly blocks actions in pre-hooks.
4. **Check all code paths**: Test both success and failure scenarios in your scripts.

## Enterprise Distribution

Enterprise organizations need to enforce security policies, compliance requirements, and development standards that individual users cannot bypass. Cascade Hooks supports this through **system-level configuration**, which takes precedence and cannot be disabled by end users without root permissions.

Deploy your mandatory `hooks.json` configuration to these OS-specific locations:

**macOS:**

```
/Library/Application Support/Windsurf/hooks.json
```

**Linux/WSL:**

```
/etc/windsurf/hooks.json
```

**Windows:**

```
C:\ProgramData\Windsurf\hooks.json
```

Place your hook scripts in a corresponding system directory (e.g., `/usr/local/share/windsurf-hooks/` on Unix systems).

### Deployment Methods

Enterprise IT teams can deploy system-level hooks using standard tools and workflows:

**Mobile Device Management (MDM)**

* **Jamf Pro** (macOS) - Deploy via configuration profiles or scripts
* **Microsoft Intune** (Windows/macOS) - Use PowerShell scripts or policy deployment
* **Workspace ONE**, **Google Endpoint Management**, and other MDM solutions

**Configuration Management**

* **Ansible**, **Puppet**, **Chef**, **SaltStack** - Use your existing infrastructure automation
* **Custom deployment scripts** - Shell scripts, PowerShell, or your preferred tooling

### Verification and Auditing

After deployment, verify that hooks are properly installed and cannot be bypassed:

```bash  theme={null}

---

← Previous: [Extract file path using jq](./extract-file-path-using-jq.md) | [Index](./index.md) | Next: [Verify system hooks are present](./verify-system-hooks-are-present.md) →