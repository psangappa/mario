**Mario on a mission**

Mario and the princess are trapped in a square grid (N*N), Mario needs to reach the princess with minimum number of steps (shortest paths), while avoiding any obstacles. Mario can move UP, DOWN, LEFT and RIGHT and can’t go outside of the grid.

***First task:***

1. Validate the given inputs 
    * max 1 mario and 1 princess.
    * minimum 1 mario and 1 princess. 
    * grid should form a square matrix.
    * the given integer 'n' should be positive number greater than 1
2. Find the shortest path to reach princess avoiding all the obstacles.
3. If you don't find a shortest path, then return any possible path if it exists.

* Inputs:

    ***n:*** grid size, 
    
        For example 3
  
    ***grid:*** n*n matrix in the form of string. Each row is separated by a comma.
		
		For example: '--m,-x-,-p-'

* Output:
	
	    (ERROR_FLAG, [PATH])
	
	For example,
	
	    (True, []) - if any of the constrains are violated. Here True is the
        (False, []) - if all paths to princess are blocked by obstacles
        (False, ['DOWN', 'DOWN', 'LEFT']) - if we find a shortest path or a possible path to princess
        
* How to use:

    Simply run input.py from save_princess package and provide inputs.
    
***Second task***

I'm exposing 3 Rest API endpoints. 

* First is to find the shortest path. This uses the algorithm writer in task1. 
* Second is to see the request logs for a particular request.
* Third is to see all request logs.

Additionally, I'm using SQLLite DB to store the requests.
 
The clients of these API's can use them in the following manner

* shortest path or Possible path if any

    URL:

        /api/v1/mario/n/grid
     
    Method:
    
        GET
    
    URL Params:
        
        Required: n = [integer]
                  grid = [alphanumeric]
                  
    Successful Responses:
    
    * URL(Shortest Path): 
    
            api/v1/mario/3/--m,-x-,-p-
        
            {
                "error_flag": false,
                "paths": [
                    "DOWN",
                    "DOWN",
                    "LEFT"
                ]
            }
        
    * URL(Possible Path): 
    
            api/v1/mario/5/m--x-,xx--x,-----,-xxxx,----p
        
            {
                "error_flag": false,
                "paths": [
                "RIGHT",
                "RIGHT",
                "DOWN",
                "DOWN",
                "LEFT",
                "LEFT",
                "DOWN",
                "DOWN",
                "RIGHT",
                "RIGHT",
                "RIGHT",
                "RIGHT"
                ]
            }
        
    * URL(No Possible Path): 
    
            api/v1/mario/5/m--x-,xx--x,-----,xxxxx,----p
        
            {
                "error_flag": false,
                "paths": []
            }
            
    Error Response:
    
    * URL: 

            api/v1/mario/5/m--x-,xx--x,-----
    
            {
                "error_flag": true,
                "paths": []
            }
        
          
* Request log data.

    URL:

        /api/v1/mario/logs 
        /api/v1/mario/logs/id
     
    Method:
    
        GET
    
    URL Params:
        
        Optional: id = [integer]
                  
    Successful Response:
        
        Examlple: /api/v1/mario/logs
    
        [
            {
                "id": 6,
                "remote_address": "127.0.0.1",
                "n": 3,
                "url": "http://host:5000/api/v1/mario/3/--m%2Cxxx%2C--p",
                "grid": "--m,-x-,--p",
                "timestamp": "2019-09-19T13:26:09.328501"
            },
            {
                "id": 7,
                "remote_address": "127.0.0.1",
                "n": 3,
                "url": "http://host:5000/api/v1/mario/3/--m%2Cxxx%2C--p",
                "grid": "--m,xxx,p-p",
                "timestamp": "2019-09-19T16:41:10.107362"
            }
        ]
        
        Examlple: /api/v1/mario/logs/6
        
        {
            "id": 6,
            "remote_address": "127.0.0.1",
            "n": 3,
            "url": "http://localhost:5000/api/v1/mario/3/--m%2Cxxx%2C--p",
            "grid": "--m,xxx,--p",
            "timestamp": "2019-09-19T13:26:09.328501"
        }
