try:
    project = find_project(project_id)
    task = create_task(task_details)
    project.add_task(task)
    notify_stakeholders(task)
    return Result.success(TaskResponse.from_entity(task))
except ProjectNotFoundError:
    return Result.failure(Error.not_found("Project", str(project_id)))
except ValidationError as e:
    return Result.failure(Error.validation_error(str(e)))