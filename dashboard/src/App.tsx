import React     from 'react';

import Grid      from '@material-ui/core/Grid';
import Container from '@material-ui/core/Container';
import Paper     from '@material-ui/core/Paper';

import Header    from './components/Header';
import Chart     from './components/Chart';

function App() {
  return (
    <div>
      <Header />
      <Container maxWidth='lg'>
        <Grid container spacing={3}>

          {/* Chart */}
          <Grid item xs={12} md={8} lg={9}>
            <Paper>
              <Chart />
            </Paper>
          </Grid>

          {/* Today */}
          <Grid item xs={12} md={4} lg={3}>
            <Paper>
              <p>Today's Performance</p>
            </Paper>
          </Grid>

          {/* Recent Visitors */}
          <Grid item xs={12}>
            <Paper>
              <p>Recent Visitors</p>
            </Paper>
          </Grid>

        </Grid>
      </Container>
    </div>
  );
}

export default App;
