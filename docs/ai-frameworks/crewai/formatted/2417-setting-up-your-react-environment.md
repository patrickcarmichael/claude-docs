---
title: "Crewai: Setting Up Your React Environment"
description: "Setting Up Your React Environment section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting Up Your React Environment


To run this React component locally, you'll need to set up a React development environment and integrate this component into a React project.

<Steps>
  <Step title="Install Node.js">
    * Download and install Node.js from the official website: [https://nodejs.org/](https://nodejs.org/)
    * Choose the LTS (Long Term Support) version for stability.
  </Step>

  <Step title="Create a new React project">
    * Open Command Prompt or PowerShell
    * Navigate to the directory where you want to create your project
    * Run the following command to create a new React project:

      ```bash  theme={null}
      npx create-react-app my-crew-app
      ```
    * Change into the project directory:

      ```bash  theme={null}
      cd my-crew-app
      ```
  </Step>

  <Step title="Install necessary dependencies">
    ```bash  theme={null}
    npm install react-dom
    ```
  </Step>

  <Step title="Create the CrewLead component">
    * Move the downloaded file `CrewLead.jsx` into the `src` folder of your project,
  </Step>

  <Step title="Modify your App.js to use the CrewLead component">
    * Open `src/App.js`
    * Replace its contents with something like this:

    ```jsx  theme={null}
    import React from 'react';
    import CrewLead from './CrewLead';

    function App() {
        return (
            <div className="App">
                <CrewLead baseUrl="YOUR_API_BASE_URL" bearerToken="YOUR_BEARER_TOKEN" />
            </div>
        );
    }

    export default App;
    ```

    * Replace `YOUR_API_BASE_URL` and `YOUR_BEARER_TOKEN` with the actual values for your API.
  </Step>

  <Step title="Start the development server">
    * In your project directory, run:

      ```bash  theme={null}
      npm start
      ```
    * This will start the development server, and your default web browser should open automatically to [http://localhost:3000](http://localhost:3000), where you'll see your React app running.
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Exporting a React Component](./2416-exporting-a-react-component.md)

**Next:** [Customization →](./2418-customization.md)
