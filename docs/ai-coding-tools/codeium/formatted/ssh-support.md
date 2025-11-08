---
title: "SSH Support"
source: ""
---

# SSH Support

The usual SSH support in VSCode is licensed by Microsoft, so we have implemented our own just for Windsurf. It does require you to have [OpenSSH](https://www.openssh.com/) installed, but otherwise has minimal dependencies, and should "just work" like you're used to. You can access SSH under `Remote-SSH` in the Command Palette, or via the `Open a Remote Window` button in the bottom left.
This extension has worked great for our internal development, but there are some known caveats and bugs:

* We currently only support SSHing into Linux-based remote hosts.

* The usual Microsoft "Remote - SSH" extension (and the [open-remote-ssh](https://github.com/jeanp413/open-remote-ssh) extension) will not work—please do not install them, as they conflict with our support.

* We don't have all the features of the Microsoft SSH extension right now. We mostly just support the important thing: connecting to a host. If you have feature requests, let us know!

* Connecting to a remote host via SSH then accessing a devcontainer on that remote host won't work like it does in VSCode. (We're working on it!) For now, if you want to do this, we recommend instead manually setting up an SSH daemon inside your devcontainer. Here is the set-up which we've found to work, but please be careful to make sure it's right for your use-case.

  1. Inside the devcontainer, run this once (running multiple times may mess up your `sshd_config`):

  ```
  sudo -s -- <<HERE
  sed -i '/SSO SSH Config START/Q' /etc/ssh/sshd_config
  echo "Port 2222" >> /etc/ssh/sshd_config
  ssh-keygen -A
  HERE
  ```

  2. Inside the devcontainer, run this in a terminal you keep alive (e.g. via tmux):

  ```
  sudo /usr/sbin/sshd -D
  ```

  3. Then just connect to your remote host via SSH in windsurf, but using the port 2222.

* SSH agent-forwarding is on by default, and will use Windsurf's latest connection to that host. If you're having trouble with it, try reloading the window to refresh the connection.

* On Windows, you'll see some `cmd.exe` windows when it asks for your password. This is expected—we'll get rid of them soon.

* If you have issues, please first make sure that you can ssh into your remote host using regular `ssh` in a terminal. If the problem persists, include the output from the `Output > Remote SSH (Windsurf)` tab in any bug reports!

---

← Previous: [Enabling Cascade access to .gitignore files](./enabling-cascade-access-to-gitignore-files.md) | [Index](./index.md) | Next: [Dev Containers](./dev-containers.md) →