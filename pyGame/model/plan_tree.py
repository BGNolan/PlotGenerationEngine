#This file contains the functionality for creating the backend storage oobject for our
#generation engine. This structure is a general tree

#Class :  Task_Node
#This class creates the object that holds each task

class Task_Node():

    def __init__(self,task):
        self.task = task
        self.parent = None
        self.children = []
        self.count = 0
        self.depth = 0
        self.x = 0
        self.y = 0

    def add_child(self,child_node):
        self.children.append(child_node)


 #This class hold all the functionality for building the Plan tree
class Plan_Tree():

    def __init__(self):
        self.nodes = {}
        self.root= None
        #NOTE: NEVER SUBTRACT FROM THIS NUMBER
        self.node_count = 0
        self.max_depth = 0
        self.x_max = 500
        self.y_max = 500

    def get_node(self,count):
        return self.nodes[count]
    #This function adds a task to the node
    #using a dictionary and a int value count to avoid collisions
    #Hooefully this makes it really fast
    def add_task(self,task,parent = None):
        self.node_count += 1
        #print("Current Count: "+str(self.__count))
        #Create new node object
        new_task_node = Task_Node(task)
        #set node index value to count of the tree
        new_task_node.count = self.node_count
        #add parent node if parent is not none
        if parent is not None:
            #Set parent to the parent of the new task node
            new_task_node.parent = parent
           #print("Parent:" + ', '.join(new_task_node.__parent.task))
            # add the child node to the parents child list
            parent.add_child(new_task_node)
            #give child correct depth
            new_depth = parent.depth +1
            new_task_node.depth = new_depth
            if new_depth > self.max_depth:
                self.max_depth = new_depth
        #if no root node exists add root node
        if(self.root == None):
            self.root = new_task_node

        #Add node to dictionary
        self.nodes[self.node_count] = new_task_node

        return "Task Added!"


    def display_all(self):
        nodes_printed =0
    #    print("Display All the nodes in the tree with its respective parent!!")
        #Print the root node
        print ("ROOT NODE: " + ', ' .join(self.root.task) + " Count: " + str(self.root.count))
        nodes_printed +=1

        #If children exist print out all the children in a preorder manner
        if bool(self.root.children) != False:
            self.display_children(self.root)


    def display_children(self, current_node):
        #Go through child array printing all children if they exist
        for child in current_node.children:
            print ("Task: " + ', '.join(child.task) + " Parent: " + ', ' .join(child.parent.task) + " Count: " +str(child.count))
            #if Children are found in child array of child, print before next child of parent
            if bool(child.children)!= False:
                self.display_children(child)


    #returns a list of plans
    def get_plan(self,node):
        #Create a empty list called plan
        plan = []
        # if the node has no parents just return that singular task
        if node.parent is None:
            #print('Here!!')
            plan.append(node.task)
            return plan
        #if parents of the node do exist
        if node.parent is not None:
            plan = self.get_parent_task(node.parent,plan)
            # Add the task of the current node to the list
            plan.append(node.task)
            return plan

    def get_parent_task(self, node, plan):
        if node is not None:
            if node.count != self.root.count:
                plan = self.get_parent_task(node.parent,plan)
            plan.append(node.task)
        return plan


   #Retunrs a count of nodes available at a given depth level designated by the variable level
    def get_depth_count(self,level):
        count = 0
        for node in self.nodes:
            if node.depth == level:
                count += 1

        return count

    def get_subtree_width(self,subRoot):
        #Max Width is always one becuase of root node
        max_width = 1
        depth_count=[0] * 100
        depth = 0
        #set root depth depth
        depth_count[depth] = 1
        depth +=1
        #get next level depth
        depth_count[depth] = len(subRoot.children)
        depth += 1
        #get depth for rest of levels
        if len(self.root.children ) > 0:
            #Do somthing

            for child in subRoot.children:
                depth_count = self.get_subtree_width_helper(child,depth_count,depth)

            #Return max width

            for width in depth_count:
                if(width > max_width):
                    max_width = width

        # return the max width
        return max_width
    def get_subtree_width_helper(self,currentNode,depth_count,depth):
        # get depth for rest of levels
        if len(currentNode.children) > 0:
            # Do somthing
            depth_count[depth] = len(currentNode.children)
            depth+=1
            for child in currentNode.children:
                depth_count = self.get_subtree_width_helper(child, depth_count, depth)
        return depth_count


    def generate_x_Y_coordinates(self,pane_width,pane_height,box_width,box_height):
        localx = 250
        localy = 0
        total_width = 0
        #horizontal box padding
        h_box_padding = 10
        #vertical box padding
        v_box_padding = 50
        calc_pane_width = 0
        calc_pane_height = 0
        #Set Coordinates for root
        self.root.x = localx
        self.root.y = localy
        subtree_pixels = [0] * len(self.root.childrem)
        #get to total width for the tree
        for child in self.root.children:
            total_width += self.getsubtree_width(child)
        calc_pane_width = ((box_width+h_box_padding)*total_width)+h_box_padding
        calc_pane_height =((box_height+v_box_padding)*self.max_depth)+v_box_padding

        #distrbute pixels to each subtree
        child_count = 0
        for child in self.root.children:
            child_width = self.getsubtree_width(child)
            ratio = child_width / total_width
            subtree_pixels[child_count] = (int)(ratio * calc_pane_width)
            child_count += 1

        #set the left and right bounds for each subtree
        subtree_left_bounds = [0] * len(self.root.children)
        subtree_right_bounds = [0] * len(self.root.children)
        child_count = 0
        for child in self.root.children:
            if(child_count == 0):
                subtree_left_bounds[child_count] = 0
                subtree_right_bounds[child_count] = subtree_pixels[child_count]- 1

            else:
                subtree_left_bounds[child_count] = subtree_right_bounds[child_count-1] -1
                subtree_right_bounds[child_count] = subtree_left_bounds[child_count] + subtree_pixels[child_count] - 1

            child_count +=1


