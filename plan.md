# Plan 1.0


1. domain_name/group/ - shows all teacher's groups.(GET, POST) Reading and adding groups.
2. domain_name/group/create/ - realized. shows all teacher's subjects with their NAMES.(GET) Reading teacher's subjects. POST Request to rhe third link
3. domain_name/group/{group_id} - shows all homeworks of the group.(PUT, DELETE) Updating and deleting group.
4. domain_name/group/{group_id}/home_work/ - shows all homeworks of the group. (GET, POST) Reading and adding homeworks.
5. domain_name/group/{group_id}/home_work/{home_work_id}/ - shows info about homework and student's marks, if they are. (GET, POST, PUT, DELETE)
Reading, adding and updating info about homework and marks.
