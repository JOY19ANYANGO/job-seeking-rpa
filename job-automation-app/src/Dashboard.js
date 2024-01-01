// src/components/Dashboard.js
import React from 'react';
import { Container, Row, Col, Card } from 'react-bootstrap';

const Dashboard = () => {
  return (
    <Container>
      <Row>
        <Col>
          <h1 className="mt-3 mb-4">Job Automation Dashboard</h1>
          <Card>
            <Card.Body>
              {/* Add your dashboard content here */}
              <p>Welcome to the Job Automation Dashboard!</p>
            </Card.Body>
          </Card>
        </Col>
      </Row>
    </Container>
  );
};

export default Dashboard;
