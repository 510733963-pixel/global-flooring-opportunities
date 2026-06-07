import React from 'react';
import { Container, Box, Typography, Button, Grid } from '@mui/material';
import { Home as HomeIcon, Search as SearchIcon, Analytics as AnalyticsIcon } from '@mui/icons-material';

const App = () => {
  return (
    <Box sx={{ minHeight: '100vh', bgcolor: '#f5f5f5' }}>
      {/* Header */}
      <Box
        sx={{
          bgcolor: 'primary.main',
          color: 'white',
          padding: '20px 0',
          boxShadow: 1,
        }}
      >
        <Container maxWidth="lg">
          <Typography variant="h4" component="h1" sx={{ fontWeight: 'bold' }}>
            🌍 Global Flooring Opportunities Center
          </Typography>
          <Typography variant="body1" sx={{ mt: 1 }}>
            Collecting, analyzing and displaying global flooring industry opportunities
          </Typography>
        </Container>
      </Box>

      {/* Main Content */}
      <Container maxWidth="lg" sx={{ py: 4 }}>
        <Grid container spacing={3}>
          {/* Card 1 */}
          <Grid item xs={12} sm={6} md={4}>
            <Box
              sx={{
                bgcolor: 'white',
                p: 3,
                borderRadius: 2,
                boxShadow: 1,
                textAlign: 'center',
              }}
            >
              <HomeIcon sx={{ fontSize: 48, color: 'primary.main', mb: 2 }} />
              <Typography variant="h6" sx={{ mb: 2 }}>
                Browse Opportunities
              </Typography>
              <Typography variant="body2" sx={{ mb: 2, color: 'gray' }}>
                Explore the latest global flooring industry opportunities
              </Typography>
              <Button variant="contained" color="primary">
                Get Started
              </Button>
            </Box>
          </Grid>

          {/* Card 2 */}
          <Grid item xs={12} sm={6} md={4}>
            <Box
              sx={{
                bgcolor: 'white',
                p: 3,
                borderRadius: 2,
                boxShadow: 1,
                textAlign: 'center',
              }}
            >
              <SearchIcon sx={{ fontSize: 48, color: 'success.main', mb: 2 }} />
              <Typography variant="h6" sx={{ mb: 2 }}>
                Smart Search
              </Typography>
              <Typography variant="body2" sx={{ mb: 2, color: 'gray' }}>
                Find the opportunities you're interested in quickly
              </Typography>
              <Button variant="contained" color="success">
                Search
              </Button>
            </Box>
          </Grid>

          {/* Card 3 */}
          <Grid item xs={12} sm={6} md={4}>
            <Box
              sx={{
                bgcolor: 'white',
                p: 3,
                borderRadius: 2,
                boxShadow: 1,
                textAlign: 'center',
              }}
            >
              <AnalyticsIcon sx={{ fontSize: 48, color: 'info.main', mb: 2 }} />
              <Typography variant="h6" sx={{ mb: 2 }}>
                Analytics
              </Typography>
              <Typography variant="body2" sx={{ mb: 2, color: 'gray' }}>
                View market trends and industry insights
              </Typography>
              <Button variant="contained" color="info">
                View Analytics
              </Button>
            </Box>
          </Grid>
        </Grid>
      </Container>

      {/* Footer */}
      <Box
        sx={{
          bgcolor: '#333',
          color: 'white',
          py: 3,
          mt: 4,
        }}
      >
        <Container maxWidth="lg">
          <Typography variant="body2" align="center">
            © 2026 Global Flooring Opportunities Center. All rights reserved.
          </Typography>
        </Container>
      </Box>
    </Box>
  );
};

export default App;
