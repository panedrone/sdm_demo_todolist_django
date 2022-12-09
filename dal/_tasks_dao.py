"""
Code generated by a tool. DO NOT EDIT.
https://sqldalmaker.sourceforge.net/
"""

from dal.task import Task


class _TasksDao:

    def __init__(self, ds):
        self.ds = ds

    def create_task(self, p):
        """
        (C)RUD: tasks
        Generated values are passed to DTO.
        :param p: Task
        :return: None
        :raises Exception: if no rows inserted.
        """
        self.ds.create_one(p)

    def read_task(self, t_id):
        """
        C(R)UD: tasks
        :param t_id: int
        :return: Task
        :raises Exception: if amount of returned rows != 1.
        """
        return self.ds.read_one(Task, {'t_id': t_id})

    def update_task(self, t_id, data):
        """
        CR(U)D: tasks
        :param t_id: int
        :param data: dict of pairs column-value
        :return: int (the number of affected rows)
        """
        self.ds.update_one(Task, data, {'t_id': t_id})

    def delete_task(self, t_id):
        """
        CRU(D): tasks
        :param t_id: int
        :return: int (the number of affected rows)
        """
        return self.ds.delete_one(Task, {'t_id': t_id})