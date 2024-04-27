import salabim as sim  # type: ignore


class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            # Customer()
            self.hold(sim.Uniform(5, 15).sample())


class Customer(sim.Component):
    def process(self):
        self.enter(waitingline)
        # if clerk.ispassive():
        #     clerk.activate()
        for clerk in clerks:
            if clerk.ispassive():
                clerk.activate()
                break  # activate one clerk at a time only
        self.passivate()


class Clerk(sim.Component):
    def process(self):
        while len(waitingline) == 0:
            self.passivate()
        self.customer = waitingline.pop()
        self.hold(30)
        self.customer.activate()


if __name__ == "__main__":
    env = sim.Environment(trace=True)
    CustomerGenerator()
    # clerk = Clerk()  # first exercise
    clerks = [Clerk() for _ in range(3)]
    clerks = sim.Queue(name="clerks", fill=[Clerk() for _ in range(3)])
    waitingline = sim.Queue("waitingline")
    env.run(till=50)
    # print()
    waitingline.print_statistics()
    # waitingline.print_info()
