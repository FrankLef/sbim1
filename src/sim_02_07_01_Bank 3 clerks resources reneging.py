import salabim as sim  # type: ignore


class CustomerGenerator(sim.Component):
    def process(self):
        while True:
            Customer()
            self.hold(sim.Uniform(5, 15).sample())


class Customer(sim.Component):
    def process(self):
        if len(clerks.requesters()) >= 5:
            env.number_balked += 1
            env.print_trace("", "", "balked")
            self.cancel()
        self.request(clerks, fail_delay=50)
        if self.failed():
            env.number_reneged += 1
            env.print_trace("", "", "reneged")
        else:
            self.hold(30)
            self.release()


if __name__ == "__main__":
    # main()
    env = sim.Environment(trace=False)
    env.number_reneged = 0
    env.number_balked = 0
    CustomerGenerator()
    clerks = sim.Resource("clerks", capacity=3)
    env.run(till=50000)
    clerks.requesters().length.print_statistics()
    clerks.requesters().length_of_stay.print_statistics()
    print("number reneged", env.number_reneged)
    print("number balked", env.number_balked)
