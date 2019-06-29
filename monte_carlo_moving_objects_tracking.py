import random
import math


alpha_1 = 1.0           # desvio padrão da velocidade padrão 0.2
alpha_2 = 0.1           # desvio padrão de theta padrão 0.01
v_min = 0.0             # velocidade mínima
v_max = 25.0            # velocidade máxima
M_PI = math.pi

def normalize_theta(theta):
    multiplier = 0
    if (theta >= -M_PI and theta < M_PI):
       return theta
   
    multiplier = (int)(theta / (2*M_PI))
    theta = theta - multiplier*2*M_PI
    if (theta >= M_PI):
       theta -= 2*M_PI
    if (theta < -M_PI):
       theta += 2*M_PI

    return theta


class Particle:
    def __init__(self, x, y, theta, velocity_x, velocity_y, dist = None, norm_dist = None, timestamp = None):
        self.x = x
        self.y = y
        self.theta = theta
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y
        self.dist = dist
        self.norm_dist = norm_dist
        self.timestamp = timestamp
        self.weight
    


    def sample_motion_model(self,delta_time):
        
        velocity_x = self.velocity_x
        velocity_y = self.velocity_y
        x = self.x
        y = self.y
        theta = self.theta        

            

        theta = theta + random.gauss(0.0, alpha_2)
        theta = normalize_theta(theta)
        
        # x = x + delta_time* velocity * math.cos(theta)
        # y = y + delta_time* velocity * math.sin(theta)

        x = x + x * velocity_x * delta_time
        y = y + y * velocity_y * delta_time

        
        velocity_x = velocity_x + random.gauss(0.0,alpha_1)
        velocity_y = velocity_y + random.gauss(0.0,alpha_1)

        if(velocity_x > v_max):
            velocity_x = v_max
        if(velocity_x < v_min):
            velocity_x = v_min

        if(velocity_y > v_max):
            velocity_y = v_max
        if(velocity_y < v_min):
            velocity_y = v_min
        


        self.velocity = velocity
        self.x = self.x
        self.y = self.y
        self.theta = normalize_theta(theta)        


    def distance_to_the_nearest_neighbor(self,obj_x, obj_y):
        distance = 0.0
        d_x, d_y = 0.0

        d_x = self.x - obj_x 
        d_y = self.y - obj_y 

        distance = math.sqrt(math.pow(d_x,2) + math.pow(d_y,2))

        return distance


def calculation_particle_weight_pose_reading_model(dist):

    particle_weight = 0.0
    particle_weight = math.exp(-dist)
    return particle_weight
    



def measurement_model(x, y, lst_particles):
    num_particles = lst_particles.length()
    lst_distance = [0.0 for i in range(num_particles)]
    sum_weights = 0.0

    
    for i in range(num_particles):
        lst_distance[i] = lst_particles[i].distance_to_the_nearest_neighbor(x,y)

    
    for i in range(num_particles):
        lst_particles[i].weight = calculation_particle_weight_pose_reading_model(lst_distance[i])
        sum_weights += lst_particles[i].weight

    
    #normalização do peso
    for i in range(num_particles):
        lst_particles[i].weight = (lst_particles[i].weight/ sum_weights)



