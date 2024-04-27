import salabim as sim  # type: ignore


class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            customer = Customer()
            self.to_store(store=waitingroom, item=customer, fail_at=env.now())
            if self.failed():
                customer.cancel()
                env.number_balked += 1
                # print(env.now(), "balked", customer.name())
                env.print_trace("", "", "balked", customer.name())
            self.hold(sim.Uniform(5, 15).sample())


class Customer(sim.Component):
    def process(self):
        self.hold(50)
        if self in waitingroom:
            self.leave(waitingroom)
            env.number_reneged += 1
            env.print_trace("", "", "reneged")


class Clerk(sim.Component):
    def process(self):
        while True:
            customer = self.from_store(waitingroom)  # noqa
            self.hold(30)


if __name__ == "__main__":
    # main()
    env = sim.Environment(trace=False)
    env.number_reneged = 0
    env.number_balked = 0
    CustomerGenerator()
    for _ in range(3):
        Clerk()
    waitingroom = sim.Store("waitingroom", capacity=5)
    env.run(till=300000)
    waitingroom.length.print_statistics()
    waitingroom.length_of_stay.print_statistics()
    print("number reneged", env.number_reneged)
    print("number balked", env.number_balked)
