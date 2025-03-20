from abstra.compat import use_legacy_threads
"""
Calling the use_legacy_threads function allows using
the legacy threads in versions > 3.0.0
https://abstra.io/docs/guides/use-legacy-threads/

The new way of using workflows is with tasks. Learn more
at https://abstra.io/docs/concepts/tasks/ and contact us
on any issues during your migration
"""
use_legacy_threads("forms")

from abstra.forms import *
from abstra.workflows import *
from abstra.tables import *


# gets the email owner information on the tables team
def team_info_by_email(email):
    stm = select_one("team", where={"company_email": email})

    return stm


# verify if the requester is a valid user
assignee_emails = get_data("assignee_emails")
data = get_data(
    "purchase_data")
description = data["description"]
amount = data["amount"]
quantity = data["quantity"]
reason = data["reason"]
deadline = data["deadline"]
requester_team_name = data["requester_team_name"]
requester_team_id = data["requester_team_id"]
requester_team_position = data["requester_team_position"]
purchase_request_id = data["purchase_request_id"]


purchase_request_status = get_data("purchase_request_status")

assignee_emails = get_data("assignee_emails")
approval_team_email = get_data("item")
if approval_team_email == None:
    approval_team_email = assignee_emails[0]

# builds the purchase approval page
approval_page = Page().display("Purchase Request Approval", size="large")\
                      .display_markdown(
    f"""

You are requested to review the following purchase request and provide your decision regarding its approval. The details of the request are as follows:
- **Description of Item(s)**: {description}
- **Total Amount**: R$ {amount}
- **Quantity Needed**: {quantity}
- **Reason for Purchase**: {reason}
- **Requested Deadline**: {deadline}
- **Submitted By**: {requester_team_name} - {requester_team_position}
- **Review Guidelines**:
1. **Budget Compatibility**: Does the requested amount align with our current budget and financial strategies?
2. **Necessity**: Is the purchase essential for the team's operations or project success?
3. **Timing**: Can the purchase wait, or is the deadline justified based on operational needs?
4. **Compliance and Procurement**: Does the request comply with our procurement policy, including seeking at least three quotes for comparison?
"""
)\
    .run(actions=["Approve", "Reject"])


if approval_page.action == "Approve":
    purchase_approved = True
else:
    purchase_approved = False
    rejection_page = Page().display("Purchase Request Rejection", size="large")\
                           .read_textarea("Reason for Rejection", key="rejection_reason")\
                           .run("Send")
    set_data("rejection_reason", rejection_page["rejection_reason"])


approval_team_id = team_info_by_email(approval_team_email)["id"]

update("purchase_request_approvals", set={"approved": purchase_approved}, 
       where={"purchase_request_id": purchase_request_id, "team_id": approval_team_id})
