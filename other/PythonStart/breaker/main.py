import pybreaker

# Used in database integration points

class DBListener(pybreaker.CircuitBreakerListener):
    "Listener used by circuit breakers that execute database operations."

    def before_call(self, cb, func, *args, **kwargs):
        "Called before the circuit breaker `cb` calls `func`."
        pass

    def state_change(self, cb, old_state, new_state):
        "Called when the circuit breaker `cb` state changes."
        msg = "State Change: CB: {0}, New State: {1}".format(cb.name, new_state)
        print(msg)

    def failure(self, cb, exc):
        "Called when a function invocation raises a system error."
        print("熔断了")
        pass

    def success(self, cb):
        "Called when a function invocation succeeds."
        print("调用成功")


db_breaker = pybreaker.CircuitBreaker(fail_max=5, reset_timeout=60)
db_breaker.add_listeners(DBListener(),)

@db_breaker
def update_customer():
    a = []
    print(a[0])


if __name__ == "__main__":
    for i in range(10):
        try:
            update_customer()
        except :
            pass

