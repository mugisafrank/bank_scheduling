import time
import random
import threading

# Customer class
class Customer:
    #cid= Customer id
    def create_customer(self, cid, priority, service_time):
        self.cid = cid
        self.priority = priority
        self.service_time = service_time

    def __str__(self):
        return f"Customer-{self.cid} (Priority: {self.priority}, Time: {self.service_time}s)"

# Agent class, aid=agent ID
class Agent:
    def create_agent(self, aid):
        self.aid = aid
        self.available = True

    def serve(self, customer):
        self.available = False
        print(f"Agent-{self.aid} serving {customer}")
        time.sleep(customer.service_time)
        print(f"Agent-{self.aid} finished serving {customer}")
        self.available = True

# Assign customers to agents
def assign_customers(customers, agents):
    for customer in customers:
        assigned = False
        while not assigned:
            for agent in agents:
                if agent.available:
                    threading.Thread(target=agent.serve, args=(customer,)).start()
                    assigned = True
                    break
            if not assigned:
                print("All agents are busy. Waiting...")
                time.sleep(1)

# Create customers
customers = []
for i in range(5):  # Create 5 customers
    customer = Customer()
    customer.create_customer(i, random.randint(1, 3), random.randint(2, 5))
    customers.append(customer)

# Create agents
agents = []
for i in range(1, 4):  # Create 3 agents
    agent = Agent()
    agent.create_agent(i)
    agents.append(agent)

# Start simulation
print("Starting simulation with 3 agents...")
assign_customers(customers, agents)

# Wait for all threads to finish
time.sleep(10)
print("All customers served.")
