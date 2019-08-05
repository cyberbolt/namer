provider "aws" {
  profile    = "default"
  region     = var.region
}

resource "aws_instance" "namer" {
  ami           = "ami-0ac05733838eabc06"
  instance_type = "t2.micro"

  provisioner "local-exec" {
    command = "echo ${aws_instance.example.public_ip} > namer_ip_address.txt"
  }
}

resource "aws_instance" "mongo" {
  ami           = "ami-0ac05733838eabc06"
  instance_type = "t2.micro"

  provisioner "local-exec" {
    command = "echo ${aws_instance.example.public_ip} > mongo_ip_address.txt"
  }
}