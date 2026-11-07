# Task 04 - Dependency Planner
def plan(tasks, deps):
    for a, b in deps:
        if a not in tasks or b not in tasks:
            raise ValueError("Unknown task")
    done = []
    while len(done) < len(tasks):
        ready = []
        for t in tasks:
            # a task is ready if all its "before" tasks are done
            waiting = [a for a, b in deps if b == t and a not in done]
            if t not in done and waiting == []:
                ready.append(t)
        if ready == []:
            raise ValueError("Cycle found")
        done.append(min(ready))               # alphabetically first
    return done

print(plan(["build", "test", "deploy"], [("build", "test"), ("test", "deploy")]))
