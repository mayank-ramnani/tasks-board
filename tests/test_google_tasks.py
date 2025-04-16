from taskboard import get_client, Task

def test_list_task_lists_and_tasks() -> None:
    client = get_client()

    task_lists = client.get_task_lists()
    print("Task Lists:")
    for tl in task_lists:
        print(f"- {tl.name} ({tl.id})")

        tasks = client.get_tasks(tl.id)
        print("  Tasks:")
        for t in tasks:
            print(f"    * {t.title} [{t.status}]")

def test_add_and_delete_task() -> None:
    client = get_client()
    task_lists = client.get_task_lists()
    assert task_lists, "No task lists available"
    list_id = task_lists[0].id

    task = Task(id="", title="Test Task", list_id=list_id)
    client.add_task(task)
    assert task.id, "Task ID was not set after add"

    tasks = client.get_tasks(list_id)
    assert any(t.id == task.id for t in tasks), "Task not found after add"

    deleted = client.delete_task(task.id)
    assert deleted, "Failed to delete task"

def test_update_task() -> None:
    client = get_client()
    task_lists = client.get_task_lists()
    assert task_lists, "No task lists available"
    list_id = task_lists[0].id

    task = Task(id="", title="Update Me", list_id=list_id)
    client.add_task(task)
    assert task.id, "Task ID was not set after add"
    task.title = "Updated Title"
    client.update_task(task)

    updated_tasks = client.get_tasks(list_id)
    found = next((t for t in updated_tasks if t.id == task.id), None)
    assert found is not None, "Updated task not found"
    assert found.title == "Updated Title", "Task title did not update"

    client.delete_task(task.id)
