terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
}

provider "azurerm" {
  features {}
}

variable "sql_admin_password" {
  type    = string
  default = "P@ssw0rd-Terraform-Pr0d-2026!"
}

resource "azurerm_mssql_server" "main" {
  name                         = "gn-sql-prod"
  resource_group_name          = "rg-prod"
  location                     = "westeurope"
  version                      = "12.0"
  administrator_login          = "sqladmin"
  administrator_login_password = var.sql_admin_password
}
