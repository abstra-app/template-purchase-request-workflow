# Purchase Request Workflow Template
## How it works:

This project includes an internal company purchase request evaluation implemented with Abstra and Python scripts. The requester fills out a form that is then sent to the responsible team for approval. The system integrates with Slack to send alerts about the request status. 

Integrations:
  - Slack

To customize this template for your team and build a lot more, [book a demonstration here.](https://meet.abstra.app/demo?url=purchase-request-workflow-template)

![A purchase request approval/rejection worklow built in Abstra](https://github.com/user-attachments/assets/979e1ecb-4a64-49ce-8105-8899303cb85e)

## Initial Configuration
To use this project, some initial configurations are necessary:

1. **Python Version**: Ensure Python version 3.9 or higher is installed on your system.
2. **Integrations**: To connect to Slack, this template uses Abstra connectors. To connect, simply open your project in [Abstra Cloud Console](https://cloud.abstra.io/projects/), add the Slack connector, and authorize it.
3. **Environment Variables**:

    The following environment variables are required for both local development and online deployment:

    - `SLACK_CHANNEL_NAME`: Slack channel where the notification about the purchase approval will be sent 
    - `FINANCE_TEAM_EMAIL`: Email of the team responsible for purchase approval
    - `MANAGER_EMAIL`: Email of the manager responsible for purchase approval if the value is too high
  
     For local development, create a `.env` file at the root of the project and add the variables listed above (as in `.env.examples`). For online deployment, configure these variables in your 
     [environment settings](https://docs.abstra.io/cloud/envvars).

5. **Dependencies**: To install the necessary dependencies for this project, a `requirements.txt` file is provided. This file includes all the required libraries.

   Follow these steps to install the dependencies:

   1. Open your terminal and navigate to the project directory.
   2. Run the following command to install the dependencies from `requirements.txt`:
  
      ```sh
      pip install -r requirements.txt
      ```
6. **Access Control**: The generated form is protected by default. For local testing, no additional configuration is necessary. However, for cloud usage, you need to add your own access rules. For more information on how to configure access control, refer to the [Abstra access control documentation](https://docs.abstra.io/concepts/access-control).
   
7. **Database configuration**: Set up your database tables in Abstra Cloud Tables according to the schema defined in `abstra-tables.json`.
   
    To automatically create the table schema, follow these steps:
  
    1. Open your terminal and navigate to the project directory.
  
    3. Run the following command to install the table schema from `abstra-tables.json`:
       ```sh
       abstra restore
       ```
  
    For guidance on creating and managing tables in Abstra, refer to the [Abstra Tables documentation](https://docs.abstra.io/cloud/tables).

8. **Local Usage**: To access the local editor with the project, use the following command:

   ```sh
      abstra editor path/to/your/project/folder/
   ```
   
## General Workflow:
To implement this system use the following scripts:

### Purchase Request Creation:
For creating a purchase request and collecting data about it, use:
  - **purchase_request.py**: Script to generate a form that collects internal company purchase requests. Based on the total value of the request, it is either automatically approved or assigned a "pending_manager" status.

### Purchase Request Processing:
For approving/rejecting a purchase request, use:
  - **approval_purchase_request.py**: Script to generate a form where the finance team can evaluate a purchase request with status "pending_manager".
  - **collect_approval_status.py**: Script to retrive the request status from the database.

### Purchase Request Notification:
For sending notifications on Slack about the requests status, use:
  
  - **send_purchase_approved.py**: Script to send a slack notification to the requester and the finance team when a request is approved.
  - **purchase_request_rejection_notification.py**: Script to send a slack notification to the requester when a request is rejected.



If you're interested in customizing this template for your team in under 30 minutes, [book a customization session here.](https://meet.abstra.app/demo?url=purchase-request-workflow-template)

