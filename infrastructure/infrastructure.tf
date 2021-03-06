resource "aws_security_group" "port_22_ingress_globally_accessible" {
    name = "port_22_ingress_globally_accessible"

    ingress { 
        from_port = 22    
        to_port = 22
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"] // global access! Don't do this for real.
    }
}

resource "aws_security_group" "port_mongo_ingress_globally_accessible" {
    name = "port_mongo_ingress_globally_accessible"

    ingress { 
        from_port = 27017    
        to_port = 27017
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"] // global access! Don't do this for real.
    }
}

resource "aws_security_group" "port_namer_ingress_globally_accessible" {
    name = "port_namer_ingress_globally_accessible"

    ingress { 
        from_port = 5000    
        to_port = 5000
        protocol = "tcp"
        cidr_blocks = ["0.0.0.0/0"] // global access! Don't do this for real.
    }
}

resource "aws_security_group" "allow_http_traffic" {
    name = "allow_http_traffic"

  ingress {
    from_port = 80
    to_port = 80
    protocol = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
    self = true
  }

  egress {
    from_port = "0"
    to_port = "0"
    protocol = "-1"
    cidr_blocks = ["0.0.0.0/0"]
    self = true
  }
}

resource "aws_instance" "namer" {
  ami           = "ami-0ac05733838eabc06"
  instance_type = "t2.micro"
  key_name = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [
    "${aws_security_group.port_22_ingress_globally_accessible.id}",
    "${aws_security_group.port_namer_ingress_globally_accessible.id}"
  ]

  depends_on = [
    aws_instance.mongo,
  ]

  provisioner "local-exec" {
    command = "echo ${aws_instance.namer.public_ip} > namer_ip_address.txt"
  }

  provisioner "file" {
    source      = "../tools/namer/namer-compose.yml"
    destination = "~/namer-compose.yml"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get remove docker docker-engine docker.io containerd runc",
      "sudo apt-get update",
      "sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository  \"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\"",
      "sudo apt-get update",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io",
      "curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o ~/docker-compose", 
      "chmod +x ~/docker-compose",
      "export M_USERNAME=${var.aws_m_username}",
      "export M_PASSWORD=${var.aws_m_password}",
      "export M_HOST=${aws_instance.mongo.public_ip}",
      "systemctl status docker.socket > docker_namer_status",
      "sudo ~/docker-compose --version",
      "sudo ~/docker-compose -f ~/namer-compose.yml up -d"
    ]
  }
}

resource "aws_instance" "mongo" {
  ami           = "ami-0ac05733838eabc06"
  instance_type = "t2.micro"
  key_name = aws_key_pair.deployer.key_name
  vpc_security_group_ids = [
    "${aws_security_group.port_22_ingress_globally_accessible.id}",
    "${aws_security_group.allow_http_traffic.id}",
    "${aws_security_group.port_mongo_ingress_globally_accessible.id}"
  ]

  connection {
    host = coalesce(self.public_ip, self.private_ip)
    type = "ssh"
    user = "ubuntu"
    private_key = "${var.aws_key}"
    #private_key = "${file("~/.keypairs/namer.pem")}"
  }
  
  provisioner "local-exec" {
    command = "echo ${aws_instance.mongo.public_ip} > mongo_ip_address.txt"
  }
  
  provisioner "file" {
    source      = "../tools/mongodb/mongodb-compose.yml"
    destination = "~/mongodb-compose.yml"
  }

  provisioner "remote-exec" {
    inline = [
      "sudo apt-get remove docker docker-engine docker.io containerd runc",
      "sudo apt-get update",
      "sudo apt-get install -y apt-transport-https ca-certificates curl gnupg-agent software-properties-common",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -",
      "sudo add-apt-repository  \"deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable\"",
      "sudo apt-get update",
      "sudo apt-get install -y docker-ce docker-ce-cli containerd.io",
      "curl -L https://github.com/docker/compose/releases/download/1.25.0/docker-compose-`uname -s`-`uname -m` -o ~/docker-compose", 
      "chmod +x ~/docker-compose",
      "mkdir -p ~/docker-data/mongodb",
      "export M_USERNAME=${var.aws_m_username}",
      "export M_PASSWORD=${var.aws_m_password}",
      "systemctl status docker.socket > docker_mongodb_status",
      "sudo ~/docker-compose --version",
      "sudo ~/docker-compose -f ~/mongodb-compose.yml up -d"
    ]
  }
}

resource "aws_key_pair" "deployer" {
  key_name   = "deploy"
  public_key = "${var.aws_pub_key}"
}