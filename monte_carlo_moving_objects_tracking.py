

class Particle:
    def __init__(self, x, y, theta, velocity, dist = None, norm_dist = None, timestamp = None):
        self.x = x
        self.y = y
        self.theta = theta
        self.velocity = velocity
        self.dist = dist
        self.norm_dist = norm_dist
        self.timestamp = timestamp
    


    def sample_motion_model(delta_time, particle_t_1, mean, mean_particle):
        ##todo