"""
This code was generated by a tool. Don't modify it manually.
http://sqldalmaker.sourceforge.net
"""

from dal.group import Group
from dal.group_li import GroupLI


class GroupsDao:

    def __init__(self, ds):
        self.ds = ds

    def read_group(self, g_id):
        """
        C(R)UD: groups
        @type g_id: int
        @rtype: Group
        @raise: Exception if amount of returned rows != 1.
        """
        return self.ds.read_one(Group, {'g_id': g_id})

    def delete_group(self, g_id):
        """
        CRU(D): groups
        @type g_id: int
        @rtype: int (the number of affected rows)
        """
        return self.ds.delete_one(Group, {'g_id': g_id})

    def get_groups(self):
        """
        @rtype: list[GroupLI]
        """
        sql = """select g.*,  
                (select count(*) from tasks where g_id=g.g_id) as g_tasks_count 
                from groups g 
                order by g.g_id"""
        _res = []

        def _map_cb(row):
            _obj = GroupLI()
            _obj.g_id = row["g_id"]  # q <- q
            _obj.g_name = row["g_name"]  # q <- q
            _obj.g_tasks_count = row["g_tasks_count"]  # q <- q
            _res.append(_obj)

        self.ds.query_all_rows(sql, [], _map_cb)
        return _res
