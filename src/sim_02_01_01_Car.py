import salabim as sim  # type: ignore


class Car(sim.Component):
    def process(self):
        while True:
            self.hold(1)


if __name__ == "__main__":
    env = sim.Environment(trace=True)
    Car()
    env.run(till=5)
