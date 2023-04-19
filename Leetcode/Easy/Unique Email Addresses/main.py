# https://leetcode.com/problems/unique-email-addresses/

def numUniqueEmails(emails):
    unique_emails = set()
    
    # This code is iterating through a list of email addresses and processing each email address to
    # extract the local name and domain name. It then removes any periods in the local name and any
    # text after a plus sign in the local name. Finally, it adds the modified email address to a set
    # of unique email addresses. The function returns the length of the set of unique email addresses.
    for email in emails:
        two_part_email = email.split("@")
        local_name = two_part_email[0].split("+")[0].replace(".", "")
        domain = two_part_email[1]
        unique_emails.add(local_name+"@"+domain)
            
    return len(unique_emails)