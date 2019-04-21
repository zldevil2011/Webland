import React, { Component } from 'react';
import {} from 'antd';
import styles from './SystemInput.less';

export default class SystemInput extends Component {
  render() {
    return (
      <div className={styles.systemInputContainer}>
        <div className={styles.header}>九里湖湿地综合监测平台</div>
        <div className={styles.menuList}>
          <div className={styles.menu}>九里湖湿地生态监测系统</div>
          <div className={styles.menu}>电子巡更系统</div>
          <div className={styles.menu}>视频监控系统</div>
        </div>
      </div>
    );
  }
}
