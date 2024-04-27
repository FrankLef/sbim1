import salabim as sim  # type: ignore


class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            Customer()
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
        while True:
            customer = self.from_store(waitingroom)
            self.hold(30)
            customer.activate()


# def main():
#     env = sim.Environment(trace=False)
#     CustomerGenerator()
#     waitingline = sim.Queue("waitingline")
#     waitingroom = sim.Store("waitingroom")
#     # clerks = [Clerk() for _ in range(3)]
#     clerks = sim.Queue(name="clerks", fill=[Clerk() for _ in range(3)])
#     env.run(till=50000)
#     waitingline.print_statistics()
#     waitingline.print_info()


if __name__ == "__main__":
    # main()
    env = sim.Environment(trace=False)
    CustomerGenerator()
    waitingline = sim.Queue("waitingline")
    waitingroom = sim.Store("waitingroom")
    clerks = [Clerk() for _ in range(3)]
    clerks = sim.Queue(name="clerks", fill=[Clerk() for _ in range(3)])
    env.run(till=50000)
    waitingline.print_statistics()
    waitingline.print_info()
