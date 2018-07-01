import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Toolbar from '@material-ui/core/Toolbar';
import AppBar from '@material-ui/core/AppBar';
import API from './api';
import { formatDate, getDateFormat, dateFromString, formatDateToISO } from '../utils';

class DirectApp extends React.Component {
  constructor(props) {
    super(props);

    const dayTimestamp = 24 * 60 * 60 * 1000;
    const yesterday = new Date();
    const today = new Date();

    yesterday.setTime(today.getTime() - dayTimestamp);

    this.state = {
      campaigns: [],
      from: formatDate(yesterday),
      to: formatDate(today)
    };

    this.$ = window.jet.jQuery;
  }

  componentDidMount() {
    this.createDatePicker('date_from', 'from');
    this.createDatePicker('date_to', 'to');
  }

  openPicker = id => {
    this.$(`#${id}`).datepicker('show');
  };

  createDatePicker = (id, stateKey) => {
    this.$(`#${id}`).datepicker({
      dateFormat: getDateFormat(),
      nextText: '',
      prevText: '',
      onSelect: (date, picker) => this.setState({ [stateKey]: date })
    });
  };

  loadReport = e => {
    e.preventDefault();

    const from = dateFromString(this.state.from);
    const to = dateFromString(this.state.to);

    const reportsFetchers = this.props.campaignsIds.map(cid => (
      API.getCampaignsReport(cid, formatDateToISO(from), formatDateToISO(to)).then(response => {
        const items = response.data;

        if (!items.length)
          return null;

        const clicks = items.reduce((sum, item) => sum + item['clicks'], 0);
        const totalCost = items.reduce((sum, item) => sum + item['total_cost'], 0) / 1000000;
        const clickAvgCost = Math.round(totalCost / clicks);

        return {
          ...items[0],
          clicks: clicks,
          total_cost: totalCost,
          clickAvgCost: clickAvgCost
        };
      })
    ));

    Promise.all(reportsFetchers).then(campaigns => this.setState({campaigns: campaigns.filter(Boolean)}));
  };

   handleFromChange = e => {
     e.preventDefault();
    this.setState({ from: e.target.value });
  };

  handleToChange = e => {
    e.preventDefault();
    this.setState({ to: e.target.value });
  };

  render() {
    const sumClicks = this.state.campaigns.reduce((sum, item) => sum + item['clicks'], 0);
    const sumTotalCost = this.state.campaigns.reduce((sum, item) => sum + item['total_cost'], 0);
    const clickAvgCost = Math.round(sumTotalCost / sumClicks);

    const { from, to } = this.state;

    return (
      <AppBar color="inherit" position="static">
        <Toolbar>
          <input
            id="date_from"
            type="text"
            defaultValue={from}
            onChange={this.handleFromChange}
          />
          <a
            style={{ marginRight: '10px' }}
            className="vDateField-link"
            onClick={e => this.openPicker('date_from')}
          >
            <span className="icon-calendar"></span>
          </a>
          <input
            id="date_to"
            type="text"
            defaultValue={to}
            onChange={this.handleToChange}
          />
          <a
            style={{ marginRight: '10px' }}
            className="vDateField-link"
            onClick={e => this.openPicker('date_to')}
          >
            <span className="icon-calendar"></span>
          </a>
          <Button variant='contained' size='small' onClick={this.loadReport}>Применить</Button>
        </Toolbar>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Кампания</TableCell>
              <TableCell>Тип</TableCell>
              <TableCell>Клики</TableCell>
              <TableCell>Расход всего</TableCell>
              <TableCell>Ср. цена клика</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.campaigns.map((item, i) => (
              <TableRow key={`opts-${i}`}>
                <TableCell scope='row'>{item['campaign_name']}</TableCell>
                <TableCell scope='row'>{item['type_name']}</TableCell>
                <TableCell scope='row'>{item['clicks'].toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{Number(item['total_cost']).toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{Math.round(item['clickAvgCost']).toLocaleString('ru-RU')}</TableCell>
              </TableRow>
            ))}
            <TableRow>
              <TableCell scope='row'>Итого:</TableCell>
              <TableCell scope='row'></TableCell>
              <TableCell scope='row'>
                {sumClicks ? sumClicks.toLocaleString('ru-RU') : null}
              </TableCell>
              <TableCell scope='row'>{sumTotalCost ? sumTotalCost.toLocaleString('ru-RU') : null}</TableCell>
              <TableCell scope='row'>{clickAvgCost ? clickAvgCost.toLocaleString('ru-RU') : null}</TableCell>
            </TableRow>
          </TableBody>
        </Table>
      </AppBar>
    );
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const campaidsIds = [...django.jQuery('.dynamic-ya_direct_campaigns .field-number input')]
    .map(input => Number(input.value))
    .filter(Boolean);

  ReactDOM.render(
    <DirectApp campaignsIds={campaidsIds} />,
    document.getElementsByClassName('direct')[0]
  );
});
