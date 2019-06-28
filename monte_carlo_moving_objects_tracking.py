import random
import math


alpha_1 = 1.0           # desvio padrão da velocidade padrão 0.2
alpha_2 = 0.1           # desvio padrão de theta padrão 0.01
v_min = 0.0             # velocidade mínima
v_max = 25.0            # velocidade máxima
M_PI = math.pi

def normalize_theta(theta):
    int multiplier
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
    def __init__(self, x, y, theta, velocity, dist = None, norm_dist = None, timestamp = None):
        self.x = x
        self.y = y
        self.theta = theta
        self.velocity = velocity
        self.dist = dist
        self.norm_dist = norm_dist
        self.timestamp = timestamp
    


    def sample_motion_model(self,delta_time):
        
        velocity = self.velocity
        x = self.x
        y = self.y
        theta = self.theta
        

        velocity = velocity + random.gauss(0.0,alpha_1)

        if(velocity > v_max):
            velocity = v_max
        if(velocity < v_min):
            velocity = v_min

        theta = theta + random.gauss(0.0, alpha_2)
        theta = normalize_theta(theta)
        
        x = x + delta_time* velocity * math.cos(theta)
        y = y + delta_time* velocity * math.sin(theta)

        self.velocity = velocity
        self.x = self.x
        self.y = self.y
        self.theta = normalize_theta(theta)        


    def distance_to_the_nearest_neighbor(self,x_z_t, y_z_t):
        distance = 0.0
        d_x, d_y = 0.0

        d_x = x_z_t - self.x
        d_y = y_z_t - self.y

        distance = math.sqrt(math.pow(d_x,2) + math.pow(d_y,2))

        return distance

    def calculation_particle_weight_pose_reading_model(dist):

        particle_weight = 0.0
        particle_weight = math.exp(-dist)
        return particle_weight
    

