variable "aws_region" {}
variable "aws_key" {}
variable "aws_access_key_id" {}
variable "aws_secret_access_key" {}
variable "aws_zones" {
 type        = "list"
 description = "List of availability zones to use"
 default     = ["eu-central-1a", "eu-central-1b", "eu-central-1c"]
}