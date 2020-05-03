import React from 'react';

import { useTheme } from '@material-ui/core/styles';
import { ResponsiveContainer } from 'recharts';

import Title from './Title';

export default function Chart() {
  const theme = useTheme();

  return (
    <React.Fragment>
      <Title>This Week</Title>
      <ResponsiveContainer>
        <p>Insert Chart</p>
      </ResponsiveContainer>
    </React.Fragment>
  );
}