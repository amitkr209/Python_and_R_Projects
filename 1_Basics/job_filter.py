
def job_posting(Location):
    for job in job_postings:
        if job['location'] == Location:
            for key, value in job.items():
                print(job['title'])
                break

job_postings = [
    {'title': 'Data Scientist', 'location': 'New York'},
    {'title': 'Data Analyst', 'location': 'San Francisco'},
    {'title': 'Machine Learning Engineer', 'location': 'New York'},
    {'title': 'Machine Learning Engineer', 'location': 'Delhi'}
]