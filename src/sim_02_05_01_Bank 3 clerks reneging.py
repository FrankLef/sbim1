import salabim as sim  # type: ignore


class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            Customer()
            self.hold(sim.Uniform(5, 15).sample())


class Customer(sim.Component):
    def process(self):
        if len(waitingline) >= 5:
            env.number_balked += 1
            env.print_trace("", "", "balked")
            print(env.now(), "balked", self.name())
            self.cancel()
        self.enter(waitingline)
        for clerk in clerks:
            if clerk.ispassive():
                clerk.activate()
                break  # activate only 1 clerk
        self.hold(50)  # if not served within this time, renege
        if self in waitingline:
            self.leave(waitingline)
            env.number_reneged += 1
            env.print_trace("", "", "reneged")
        else:
            self.passivate()  # wait for service to be completed


class Clerk(sim.Component):
    def process(self):
        while True:
            while len(waitingline) == 0:
                self.passivate()
            self.customer = waitingline.pop()
            self.customer.activate()  # get the cutomer out of it's hold(50)
            self.hold(30)
            self.customer.activate()  # signal the customer it's done


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
    env.number_reneged = 0
    env.number_balked = 0
    clerks = [Clerk() for _ in range(3)]
    waitingline = sim.Queue("waitingline")
    env.run(till=300000)
    waitingline.length.print_statistics()
    waitingline.length_of_stay.print_statistics()
    print("number reneged", env.number_reneged)
    print("number balked", env.number_balked)
