provider "aws" {
  region = "us-east-1"
}

resource "aws_ecs_cluster" "cluster" {
  name = "jwt-validator-cluster"
}

resource "aws_ecs_service" "service" {
  name            = "jwt-validator-service"
  cluster         = aws_ecs_cluster.cluster.id
  desired_count   = 1
  launch_type     = "FARGATE"
  
  network_configuration {
    subnets          = ["subnet-12345"]
    security_groups  = ["sg-12345"]
  }
  
  task_definition = aws_ecs_task_definition.jwt_validator_task.arn
}

resource "aws_ecs_task_definition" "jwt_validator_task" {
  family                   = "jwt-validator-task"
  requires_compatibilities = ["FARGATE"]
  network_mode             = "awsvpc"

  container_definitions = <<DEFINITION
[
  {
    "name": "jwt-validator",
    "image": "your-docker-image",
    "cpu": 256,
    "memory": 512,
    "essential": true,
    "portMappings": [
      {
        "containerPort": 8000,
        "hostPort": 8000
      }
    ]
  }
]
DEFINITION
}
