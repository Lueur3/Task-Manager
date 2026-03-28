import pytest
import src.models as md


@pytest.fixture()
def sample_task():
    task = md.Task(
        "Update Portfolio",
        "Add the latest project case studies, refresh the tech stack list, and double-check all live links for errors.",
        False,
    )
    return task


@pytest.fixture()
def empty_todo_list():
    return md.ToDoList()


@pytest.fixture()
def populated_todo_list():
    todo_list = md.ToDoList()
    task1 = md.Task(
        "Update Portfolio",
        "Add the latest project case studies, refresh the tech stack list, and double-check all live links for errors.",
        False,
    )
    task2 = md.Task(
        "Book Flight Tickets",
        "Compare prices for the upcoming vacation, select a direct flight, and confirm the booking before the sale ends.",
        False,
    )
    task3 = md.Task(
        "Weekly Grocery Shopping",
        "Make a list of essentials, visit the local market, and prep meals for the next three days.",
    )
    task4 = md.Task(
        "Finish Online Course",
        "Watch the final two modules on data visualization and take the short quiz to receive the certificate.",
        True,
    )
    todo_list.add_task(task3)
    todo_list.add_task(task2)
    todo_list.add_task(task1)
    todo_list.add_task(task4)

    return todo_list


@pytest.mark.parametrize(
    "title, descr, exp_stat",
    [
        (
            "Fix Kitchen Faucet",
            "Buy a new washer at the hardware store and replace the leaking part in the sink to stop the dripping.",
            False,
        )
    ],
)
def test_task_init(title, descr, exp_stat):
    task = md.Task(title, descr)
    assert task.title == title
    assert task.description == descr
    assert task.is_done == exp_stat


def test_task_mark_mode(sample_task):
    sample_task.mark_done()
    assert sample_task.is_done == True


@pytest.mark.parametrize(
    "exp_dc",
    [
        {
            "title": "Update Portfolio",
            "description": "Add the latest project case studies, refresh the tech stack list, and double-check all live links for errors.",
            "is_done": False,
        }
    ],
)
def test_task_to_dict(sample_task, exp_dc):
    dc = sample_task.to_dict()
    assert dc == exp_dc


@pytest.mark.parametrize(
    "dc",
    [
        {
            "title": "Update Portfolio",
            "description": "Add the latest project case studies, refresh the tech stack list, and double-check all live links for errors.",
            "is_done": False,
        }
    ],
)
def test_task_from_dict(dc, sample_task):
    task = md.Task.from_dict(dc)
    assert task.__dict__ == sample_task.__dict__


@pytest.mark.parametrize("exp_out", ["Task: Update Portfolio Status: False"])
def test_task_str(sample_task, exp_out):
    assert str(sample_task) == exp_out


def test_todo_init(empty_todo_list):
    assert empty_todo_list.tasks == []


def test_todo_add_task(empty_todo_list, sample_task):
    empty_todo_list.add_task(sample_task)
    assert len(empty_todo_list.tasks) > 0


@pytest.mark.parametrize("index", [2])
def test_todo_get_task(populated_todo_list, index, sample_task):
    task = populated_todo_list.get_task(index)
    assert task.title == sample_task.title
    assert task.description == sample_task.description
    assert task.is_done == sample_task.is_done


@pytest.mark.parametrize("index", [2])
def test_todo_del_task(populated_todo_list, index, sample_task):
    populated_todo_list.remove_task(index)
    assert sample_task not in populated_todo_list.tasks


@pytest.mark.parametrize("index", [-1, 999])
def test_todo_valid_idx_remove(populated_todo_list, index):
    with pytest.raises(ValueError):
        populated_todo_list.remove_task(index)


@pytest.mark.parametrize("index", [-1, 999])
def test_todo_valid_idx_get(populated_todo_list, index):
    with pytest.raises(ValueError):
        populated_todo_list.get_task(index)
