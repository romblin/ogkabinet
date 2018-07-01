import React from 'react';
import ReactDOM from 'react-dom';
import Button from '@material-ui/core/Button';
import Table from '@material-ui/core/Table';
import TextField from '@material-ui/core/TextField';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Toolbar from '@material-ui/core/Toolbar';
import AppBar from '@material-ui/core/AppBar';
import API from './api';
import _ from 'underscore';
import { formatDate, getDateFormat, dateFromString, formatDateToISO } from '../utils';

class MetrikaApp extends React.Component {

  constructor(props) {
    super(props);

    const dayTimestamp = 24 * 60 * 60 * 1000;
    const yesterday = new Date();
    const today = new Date();

    yesterday.setTime(today.getTime() - dayTimestamp);

    this.state = {
      from: formatDate(yesterday),
      to: formatDate(today),
      reports: []
    };
    this.$ = window.jet.jQuery;
  }

  componentDidMount() {
    this.createDatePicker('date_from', 'from');
    this.createDatePicker('date_to', 'to');
  }

  openPicker = id => {
    this.$(`#metrika_${id}`).datepicker('show');
  };

  createDatePicker = (id, stateKey) => {
    this.$(`#metrika_${id}`).datepicker({
      dateFormat: getDateFormat(),
      nextText: '',
      prevText: '',
      onSelect: (date, picker) => this.setState({ [stateKey]: date })
    });
  };

  handleFromChange = e => {
     e.preventDefault();
    this.setState({ from: e.target.value });
  };

  handleToChange = e => {
    e.preventDefault();
    this.setState({ to: e.target.value });
  };

  loadReport = e => {
    e.preventDefault();

    const from = dateFromString(this.state.from);
    const to = dateFromString(this.state.to);

    API.getSourcesSummary(this.props.metrikaSourceId, formatDateToISO(from), formatDateToISO(to)).then(response => {
      let docs = response.data;

      const docsWithGroups = _.reject(docs, doc => _.isNull(doc.group_id)).sort((doc1, doc2) => {
        if (doc1.group_id < doc2.group_id)
          return -1;
        else if (doc1.group_id > doc2.group_id)
          return 1;
        else
          return 0;
      });
      const docsWithoutGroups = docs.filter(doc => _.isNull(doc.group_id)).sort((doc1, doc2) => {
        if (doc1.rid < doc2.rid)
          return -1;
        else if (doc1.rid > doc2.rid)
          return 1;
        else
          return 0;
      });

      const docsGroups = _.groupBy(docsWithGroups, doc => doc.group_id);

      function createReportDoc(name, docs) {
        return {
          source: name,
          visits: docs.reduce((s, d) => s + d['visits'], 0),
          usersCnt: docs.reduce((s, d) => s + d['users_count'], 0),
          bounceRate: docs.reduce((s, d) => s + d['bounce_rate'], 0),
          pageDepth: docs.reduce((s, d) => s + d['page_depth'], 0),
          avgVisitDuration: docs.reduce((s, d) => s + d['avg_visit_duration'], 0)
        };
      }

      let reports = Object.keys(docsGroups).map(groupId => {
        const docs = docsGroups[groupId];
        return createReportDoc(docs[0]['group_name'], docs);
      });

      docs = _.groupBy(docsWithoutGroups, doc => doc.rid);
      reports.concat(Object.keys(docs, rId => {
        const docs = docs[rId];
        return createReportDoc(docs[0]['name'], docs);
      }));
      this.setState({reports: reports});
    });
  };

  render() {
    const { from, to } = this.state;

    return (
      <AppBar color='inherit' position='static'>
        <Toolbar>
          <input
            id="metrika_date_from"
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
            id="metrika_date_to"
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
          <Button onClick={this.loadReport} size='small' variant='contained'>Применить</Button>
        </Toolbar>
        <Table>
          <TableHead>
            <TableRow>
              <TableCell>Источник</TableCell>
              <TableCell>Визиты</TableCell>
              <TableCell>Посетители</TableCell>
              <TableCell>Отказы</TableCell>
              <TableCell>Глубина просмотра</TableCell>
              <TableCell>Время на сайте</TableCell>
            </TableRow>
          </TableHead>
          <TableBody>
            {this.state.reports.map((report, i) => (
              <TableRow key={`opts-${i}`}>
                <TableCell scope='row'>{report.source}</TableCell>
                <TableCell scope='row'>{report.visits.toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{report.usersCnt.toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{report.bounceRate.toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{Math.round(report.pageDepth).toLocaleString('ru-RU')}</TableCell>
                <TableCell scope='row'>{Math.round(report.avgVisitDuration).toLocaleString('ru-RU')}</TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </AppBar>
    );
  }
}

document.addEventListener('DOMContentLoaded', () => {
  const metrikaSourceId = Number(django.jQuery('#id_metrika_source_id')[0].value);
  ReactDOM.render(<MetrikaApp metrikaSourceId={metrikaSourceId} />, document.getElementsByClassName('metrika')[0])
});