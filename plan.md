# Plan 1.0


1. domain_name/group/ - **REALIZED**
   * GET - get teacher's groups(name, subject)
   * POST - create new group

2. domain_name/group/{group_id} - **REALIZED**
   * PUT - udpate info about group
   * DELETE - delete group

4. domain_name/group/{group_id}/home_work/ - **REALIZED**
   * GET - get assignments of the group
   * POST - create assignment to the group
   ```json
     {
     "lol": "int",
     "assign_deadline": "str",
     "assign_text": "str"
     }
   ```

5. domain_name/group/{group_id}/home_work/{home_work_id}/
     (GET, POST, PUT, DELETE) Reading, adding and updating info about homework and marks.
   * GET - get info about assignment

6. domain_name/group/create/ - **REALIZED**
   * GET - get teacher's subjects(id, name)

3. domain_name/group/{group_id}/student/
   * GET - get group's students

7. domain_name/subject/ - show all available subjects. (GET) Reading subjects.
