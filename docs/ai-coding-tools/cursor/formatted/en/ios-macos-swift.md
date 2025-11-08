---
title: "iOS & macOS (Swift)"
source: "https://docs.cursor.com/en/guides/languages/swift"
language: "en"
language_name: "English"
---

# iOS & macOS (Swift)
Source: https://docs.cursor.com/en/guides/languages/swift

Integrate Cursor with Xcode for Swift development

Welcome to Swift development in Cursor! Whether you're building iOS apps, macOS applications, or server-side Swift projects, we've got you covered. This guide will help you set up your Swift environment in Cursor, starting with the basics and moving on to more advanced features.

## Basic Workflow

The simplest way to use Cursor with Swift is to treat it as your primary code editor while still relying on Xcode for building and running your apps. You'll get great features like:

* Smart code completion
* AI-powered coding assistance (try [CMD+K](/en/inline-edit/overview) on any line)
* Quick access to documentation with [@Docs](/en/context/@-symbols/@-docs)
* Syntax highlighting
* Basic code navigation

When you need to build or run your app, simply switch to Xcode. This workflow is perfect for developers who want to leverage Cursor's AI capabilities while sticking to familiar Xcode tools for debugging and deployment.

### Hot Reloading

When using Xcode workspaces or projects (instead of opening a folder directly in Xcode), Xcode can often ignore changes to your files that were made in Cursor, or outside of Xcode in general.

While you can open the folder in Xcode to resolve this, you may need to use a project for your Swift development workflow.

A great solution to this is to use [Inject](https://github.com/krzysztofzablocki/Inject), a hot reloading library for Swift that allows your app to "hot reload" and update as soon as changes are made in real time. This does not suffer from the side effects of the Xcode workspace/project issue, and allows you to make changes in Cursor and have them reflected in your app immediately.

<CardGroup cols={1}>
  <Card title="Inject - Hot Reloading for Swift" horizontal icon="fire" href="https://github.com/krzysztofzablocki/Inject">
    Learn more about Inject and how to use it in your Swift projects.
  </Card>
</CardGroup>

## Advanced Swift Development

<Note>
  This section of the guide was heavily inspired by [Thomas
  Ricouard](https://x.com/Dimillian) and his
  [article](https://dimillian.medium.com/how-to-use-cursor-for-ios-development-54b912c23941)
  about using Cursor for iOS development. Please check his article for more
  details and drop him a follow for more Swift content.
</Note>

If you are looking to only need one editor open at a time, and want to avoid the need to switch between Xcode and Cursor, you can use an extension like [Sweetpad](https://sweetpad.hyzyla.dev/) to integrate Cursor directly with Xcode's underlying build system.

Sweetpad is a powerful extension that allows you to build, run and debug your Swift projects directly in Cursor, without compromising on Xcode's features.

To get started with Sweetpad, you'll still need to have Xcode installed on your Mac - it's the foundation of Swift development. You can download Xcode from the [Mac App Store](https://apps.apple.com/us/app/xcode/id497799835). Once you have Xcode set up, let's enhance your development experience in Cursor with a few essential tools.

Open your terminal and run:

```bash  theme={null}

---

← Previous: [Python](./python.md) | [Index](./index.md) | Next: [JetBrains](./jetbrains.md) →