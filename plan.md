# Plan 1.0


1. domain_name/group/ - shows all teacher's groups.(GET, POST) Reading and creating groups.
2. domain_name/group/create/ - REALIZED. shows all teacher's subjects with their NAMES.
   (GET) Reading teacher's subjects.
3. domain_name/group/{group_id} - REALIZED. Updating and deleting group (PUT, DELETE) 
4. domain_name/group/{group_id}/home_work/ - shows all homeworks of the group.
   (GET, POST) Reading and adding homeworks.
5. domain_name/group/{group_id}/home_work/{home_work_id}/ - shows info about homework and student's marks, if they are.
   (GET, POST, PUT, DELETE) Reading, adding and updating info about homework and marks.
6. domain_name/my_subjects/ - show all teachers subjects. (GET, POST) Reading and adding subjects.
7. domain_name/my_subject/add/ - show all available subjects. (GET) Reading subjects.
