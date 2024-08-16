## How it works:

This project includes an internal company purchase request evaluation implemented with Abstra and Python scripts. The requester fills out a form that is then sent to the responsible team for approval. The system integrates with Slack to send alerts about the request status. To customize this template for your team and build a lot more, [book a demonstration here.](https://meet.abstra.app/demo?url=purchase-request-workflow-template)

This template integrates with Slack. To make these integrations work, you must add your own API Keys for these services.

API Keys required:

- `SLACK_BOT_TOKEN`

## Workflow Stages:
![A purchase request approval/rejection worklow built in Abstra](https://github.com/user-attachments/assets/979e1ecb-4a64-49ce-8105-8899303cb85e)

## Stages Overview:
### Purchase Request (Forms):
  - A form to collect internal company purchase requests.
  - The amount and quantity are requested.
  - Based on the total value of the request, it is either automatically approved or assigned a "pending_manager" status.

### Approval Purchase Request (Forms):
  - If the request status is "pending_manager," a form is sent to the responsible individuals for approval.
  - The approval/rejection is recorded in a database.

### Collect Approval Status (Script):
  - The approval/rejection status of the request is retrieved from the database and sent to the next stages of the workflow.

### Purchase Request Rejection Notification (Script):
  - If the request is rejected, an alert is sent via Slack to the requester.

### Send Purchase Approval Notification (Script):
  - If the request is approved, an alert is sent via Slack to the requester and the finance team.

## Database Schema:
`payables`:
|updated_at|description|amount|purchase_request_id|
|:-:|:-:|:-:|:-:|
|```timestamp```|```str```|```int```|```str```|

`purchase_request_approvals`:
|approved|purchase_request_id|team_id|
|:-:|:-:|:-:|
|```bool```|```str```|```str```|

`purchase_requests`:
|id|created_at|
|:-:|:-:|
|```str```|```timestamp```|

`team`:
|name|intern_email|position|
|:-:|:-:|:-:|
|```str```|```str```|```str```|

If you're interested in customizing this template for your team in under 30 minutes, [book a customization session here.](https://meet.abstra.app/demo?url=purchase-request-workflow-template)
