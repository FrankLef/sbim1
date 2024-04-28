import salabim as sim  # type: ignore
# This is a test

class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            Customer()
            self.hold(sim.Uniform(5, 15).sample())


class Customer(sim.Component):
    def process(self):
        self.enter(waitingline)
        worktodo.trigger(max=1)
        self.passivate()


class Clerk(sim.Component):
    def process(self):
        while True:
            if len(waitingline) == 0:
                self.wait((worktodo, True, 1))
            self.customer = waitingline.pop()
            self.hold(30)
            self.customer.activate()


if __name__ == "__main__":
    # main()
    env = sim.Environment(trace=False)
    CustomerGenerator()
    waitingline = sim.Queue("waitingline")
    worktodo = sim.State("worktodo")
    env.run(till=50000)
    waitingline.print_histograms()
    worktodo.print_histograms()
