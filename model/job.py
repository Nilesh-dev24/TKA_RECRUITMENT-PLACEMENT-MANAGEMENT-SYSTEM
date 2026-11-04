
class Job:

    def __init__(
        self,
        company_id,
        job_title,
        technology,
        openings,
        location,
        package_lpa,
        min_percentage,
        passing_year,
        max_backlogs,
        deadline
    ):
        self.company_id = company_id
        self.job_title = job_title
        self.technology = technology
        self.openings = openings
        self.location = location
        self.package_lpa = package_lpa
        self.min_percentage = min_percentage
        self.passing_year = passing_year
        self.max_backlogs = max_backlogs
        self.deadline = deadline
