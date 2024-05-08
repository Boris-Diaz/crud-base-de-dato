import { Navbar, Nav, Container } from "react-bootstrap";
import {Link, Outlet } from "react-router-dom";



const NavbarPincipal =()=> {
  

    return (
      <div className="background">
        <Navbar  className="navBg" bg="black"  data-bs-theme="dark"  expand="lg">
          <Container fluid>
       
          <Navbar.Toggle  aria-controls="basic-navbar-nav" />
          <Navbar.Collapse id="basic-navbar-nav"> 
          <Nav className="me-auto">
          <Navbar.Brand as={Link}to="home">BMD ENGINEER SOLUTIONS</Navbar.Brand>
            <Nav.Link id='inicio' as={Link}to="home">Inicio</Nav.Link>
            <Nav.Link id='actividad' as={Link}to="actividades">Actividades</Nav.Link>
           
          </Nav>
          </Navbar.Collapse>
        </Container>
       
      </Navbar>
      
       <section>
        <Outlet/>
       </section>
      
      </div>
    )
  }


export default NavbarPincipal